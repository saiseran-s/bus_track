import paho.mqtt.client as mqtt
import ast
import time as L
import datetime 
from datetime import *
from datetime import datetime

import pymongo
from pymongo import MongoClient
import json


#dictionary containing bus_numbers of respective card numbers
bus_dic = {4612:108,3452:215,1265:322,8760:223}

def on_connect(client, userdata, flags, rc ):
	print ("connected")
	(result,mid) = mqttClient.subscribe(SUB_TOPIC)


def on_message(client, userdata, msg):
	

	message = ast.literal_eval(msg.payload.decode("utf-8") )
	print("received")
	print(message)

	try:

		if (message["sender"] == "app"):
			if (message['type'] == "req"):
				if (message["subtype"] == "busCount"):

					print("ok_app_1")
					#  do mongodb count get operation
					d = date.today()
					dt = datetime.combine(d, datetime.min.time())
					# incount  = db.col2.find({"status":"IN", "datetime":{"$gt":dt}},{"bus_no":1,"_id":0}).count()
					# outcount = db.col2.find({"status":"OUT", "datetime":{"$gt":dt}},{"bus_no":1,"_id":0}).count()
					incount  = db.col2.find({"status":"IN"},{"bus_no":1,"_id":0}).count()
					outcount = db.col2.find({"status":"OUT"},{"bus_no":1,"_id":0}).count()

					pubMessage = {"sender":"server","type":"resp","subtype":"busCount","Message":{"inCount":incount,"outCount":outcount}}
					pubMessage = json.dumps(pubMessage)
					mqttClient.publish(PUB_TOPIC,pubMessage)
					L.sleep(5)
				elif (message["subtype"] == "dayWiseStats"):

				# '''
				# 	assuming date received is a string
				# 	format of received string is : "YYYY-MM-DD"
				# 	now convert this string to integers
				# '''
				# '''
				# 	s = "YYYY-MM-DD"
				# 	date = (int, s.split('-'))
				# 	Y=int(date[1][0])
				# 	M=int(date[1][1])
				# 	D=(intdate[1][2])
				# 	day_wise_find = db.collection.find({"datetime":datetime.datetime(Y, M, D)},{"_id":0})
				# '''
					s=message['Message']["pickDate"]
					da = (int, s.split('.'))
					D=int(da[1][0])
					M=int(da[1][1])
					Y=int(da[1][2])
					print("year",Y,"month", M,"say", D)


					day_wise_find = db.collection.find({"datetime":{"$gte":datetime(Y, M, D)}},{"_id":0,})
					req = {}
					for v in day_wise_find:
						req.update({v["bus_no"]:[]})
					day_wise_find = db.collection.find({"datetime":{"$gte":datetime(Y, M, D)}},{"_id":0,})

					for val in day_wise_find:
						print("hi")
						req[val["bus_no"]].append([val["status"],str(val["datetime"])])


					pubMessage = {"sender":"server","type":"resp","subtype":"dayWiseStats","Message":req}
					pubMessage = json.dumps(pubMessage)
					mqttClient.publish(PUB_TOPIC,pubMessage)	
		elif (message['sender'] == 'device'):
			print("ok_1")
			if (message['type'] == 'req'):
				print("ok_2")
				if(message['subtype'] == "busEntry"):
					print("ok_3")
					if(message["Message"]['card_no'] in bus_dic.keys()):
						print("ok_4")
						find_count = 0
						a=L.localtime(L.time())#forms a time_struc l
						r = a.tm_year
						t = a.tm_mon
						y = a.tm_mday
						c_num = bus_dic[message["Message"]["card_no"]]#GIVES A INTEGER VALUE FROM THE DICTIONARY
						print("ok_5",c_num)
						while(find_count==0):
							print(y)
							find_status = db.collection.find({"bus_no":c_num, "datetime":{'$gt':datetime(r, t, y, 0, 0)}},{"_id":0,"status":1}).sort([("datetime", pymongo.DESCENDING)]).limit(1)#check status of the bus i.e, IN or OUT
							for val in find_status:
								print(val)
							find_count = find_status.count()
							print(find_count)
							y-= 1
							print(y)
							print("ok_6")
							print(find_status)
							for val in find_status:
								print(val)
								
							print("ok_7")

							#condition for if count  = 0 should be written
						if val["status"] == "IN":
							
							d = db.collection.insert_one({"bus_no":c_num,"status":"OUT","datetime":datetime.now()})
							print("in in",d)

							col2_cnt = db.col2.find({"bus_no":c_num, "datetime":{"$gt":datetime(r, t, y, 0, 0)}}).count()
							print(int(col2_cnt))
							if (int(col2_cnt) == 0):
								new_entry = db.col2.insert_one({"bus_no":c_num,"status":"OUT","datetime":datetime.now()}).inserted_id
								
								print("inserted :",new_entry)

							elif (int(col2_cnt) >=1):
								try:	
									re_update = db.col2.find_one_and_update({"bus_no":c_num,"status":"IN","datetime":{"$gt":datetime(r, t, y)}},{"$set":{"status":"OUT", "datetime":datetime.now()}}, upsert=True).inserted_id	
								except Exception as e:
									print (e,"ok_7 after error")	
									print("updated :",re_update)
						
						elif val["status"] =="OUT": #set status to "IN" and insert
							d = db.collection.insert_one({"bus_no":c_num,"status":"IN","datetime":datetime.now()}).inserted_id
							print("in out",d)
							col2_cnt = db.col2.find({"bus_no":c_num, "datetime":{"$gt":datetime(r, t, y, 0, 0)}}).count()
							print(col2_cnt)
							if (int(col2_cnt) == 0):
								new_entry = db.col2.insert_one({"bus_no":c_num,"status":"IN","datetime":datetime.now()}).inserted_id
								print("inserted :",new_entry)
							elif (int(col2_cnt) >=1):
								re_update = db.col2.find_one_and_update({"bus_no":c_num,"status":"OUT","datetime":{"$gt":datetime(r, t, y)}},{"$set":{"status":"IN", "datetime":datetime.now()}}, upsert=True).inserted_id
								print("updated :",re_update)


	except Exception as e:
		print (e)



			


	


def mqttInit():
	global mqttClient
	# 1.3 Initializing mqtt client
	mqttClient = mqtt.Client()

	mqttClient.connect(hostname,port,timealive)

	mqttClient.on_connect = on_connect
	mqttClient.on_message = on_message
	mqttClient.loop_start()
	mqttClient.loop_forever()

if __name__ == '__main__':
	hostname  = '192.168.99.236'
	port      = 1883
	timealive = 60
	
	PUB_TOPIC = "bT-App"
	SUB_TOPIC = "bT-Server"


	mongo_conn = MongoClient('localhost:27017')

	db = mongo_conn.bus_track
	collection = db.bt_arr_dep_data

	mqttInit()




