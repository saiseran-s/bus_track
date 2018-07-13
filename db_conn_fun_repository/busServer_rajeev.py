import paho.mqtt.client as mqtt
import ast
import time
import datetime
from datetime import timedelta
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
					justDate = date.today()
					dateWithMinTime = justDate.replace(hour=0, minute=0, second=0, microsecond=0) 
					incount  = db.col2.find({"status":"IN", "datetime":{"$in":dateWithMinTime}},{"bus_no":1,"_id":0}).count()
					outcount = db.col2.find({"status":"OUT", "datetime":{"$in":dateWithMinTime}},{"bus_no":1,"_id":0}).count()

					pubMessage = {"sender":"server","type":"resp","subtype":"busCount","Message":{"inCount":incount,"outCount":outcount}}
					pubMessage = json.dumps(pubMessage)
					mqttClient.publish(PUB_TOPIC,pubMessage)
					time.sleep(5)

		elif (message['sender'] == 'device'):
			if (message['type'] == 'req'):
				if(message['subtype'] == "busEntry"):
					if(message["Message"]['card_no'] in bus_dic.keys()):
						vehicle_number = bus_dic[message["Message"]['card_no']]

						find_count = 0

						
						c_num = bus_dic[message["Message"]["card_no"]]#GIVES A INTEGER VALUE FROM THE DICTIONARY
						justDate = date.today()

						# Looping through the DB till we find the last update for a particular BUS 
						while(find_count==0):
							dateWithMinTime = justDate.replace(hour=0, minute=0, second=0, microsecond=0) 

							find_status = db.collection.find({"bus_no":vehicle_number,"datetime":{'$in':dateWithMinTime}},{"_id":0,"status":1}).sort([("datetime", pymongo.DESCENDING)]).limit(1)
							find_count = find_status.count()
					
							print(find_count)

							justDate = date.today() - timedelta(days=1)

							print(find_status)
							
							for val in find_status:
								print(val)
								pass
							
							if val["status"] == "IN":
								
								# Usual Bus Entry/Exit Insert the Collection 1
								d = db.collection.insert_one({"bus_no":vehicle_number,"status":"OUT","datetime":datetime.now()})
								print("in in",d)

								justDate = date.today()
								dateWithMinTime = justDate.replace(hour=0, minute=0, second=0, microsecond=0) 
						
								col2_cnt = db.col2.find({"bus_no":vehicle_number,"datetime":{"$in":dateWithMinTime}}).count()
								
								# Bus Entry/Exit Status update for the collection 2
								if (int(col2_cnt) == 0):
									new_entry = db.col2.insert_one({"bus_no":vehicle_number,"status":"OUT","datetime":datetime.now()}).inserted_id
									
									print("inserted :",new_entry)

								elif (int(col2_cnt) >=1):
									try:	
										re_update = db.col2.find_one_and_update({"bus_no":vehicle_number,"status":"IN","datetime":{"$in":dateWithMinTime}},{"$set":{"status":"OUT", "datetime":datetime.now()}}, upsert=True).inserted_id	
									except Exception as e:
										print (e,"ok_7 after error")	
										print("updated :",re_update)
							
							elif val["status"] =="OUT": #set status to "IN" and insert
								d = db.collection.insert_one({"bus_no":vehicle_number,"status":"IN","datetime":datetime.now()}).inserted_id
								print("in out",d)
								col2_cnt = db.col2.find({"bus_no":vehicle_number ,"datetime":{"$gt":datetime(r, t, y, 0, 0)}}).count()
								print(col2_cnt)
								if (int(col2_cnt) == 0):
									new_entry = db.col2.insert_one({"bus_no":vehicle_number,"status":"IN","datetime":datetime.now()}).inserted_id
									print("inserted :",new_entry)
								elif (int(col2_cnt) >=1):
									re_update = db.col2.find_one_and_update({"bus_no":vehicle_number,"status":"OUT","datetime":{"$gt":datetime(r, t, y)}},{"$set":{"status":"IN", "datetime":datetime.now()}}, upsert=True).inserted_id
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
	hostname  = 'localhost'
	port      = 1883
	timealive = 60
	
	PUB_TOPIC = "bT-App"
	SUB_TOPIC = "bT-Server"


	mongo_conn = MongoClient('localhost:27017')

	db = mongo_conn.bus_track
	collection = db.bt_arr_dep_data

	mqttInit()




