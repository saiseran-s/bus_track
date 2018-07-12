import paho.mqtt.client
import ast
import time
import datetime
from datetime import *
from pymongo import MongoClient


#dictionary containing bus_numbers of respective card numbers
bus_dic = {4612:108,3452:215,1265:322,8760:223}

def on_connect(client, userdata, flags, rc ):
	print ("connected")
	(result,mid) = mqttClient.subscribe(SUB_TOPIC)


def on_message(client, userdata, msg):
	print msg.keys()
	message = ast.literal_eval(msg.payload)
'''
received message format : message = {
										"sender":"<sender_name>",
								  		" type":"req",
								  		"subType":"<type of request>"
								  	}
'''
	if (message["sender"] == "app"):
		if (message['type'] == "req")
			if (message["subType"] == "busCount"):

				#  do mongodb count get operation

				incount  = db.collection.find({"status":"IN"},{"bus_no":1,"_id":0}).count()
				outcount = db.collection.find({"status":"OUT"},{"bus_no":1,"_id":0}).count()

				pubMessage = {"sender":"server","type":"resp","subType":"busCount","Message":{"inCount":incount,"outCount":outcount}}
				mqttClient.publish(PUB_TOPIC,pubMessage)

			else if (message["subType"] == "dayWiseStats"):
				'''
					assuming date received is a string
					format of received string is : "YYYY-MM-DD"
					now convert this string to integers
				'''
				'''
					s = "YYYY-MM-DD"
					date = (int, s.split('-'))
					Y=int(date[1][0])
					M=int(date[1][3])
					D=(intdate[1][0])
					day_wise_find = db.collection.find({"datetime":datetime.datetime(Y, M, D)},{"_id":0})
				'''
				day_wise_find = db.collection.find({"datetime":<date>},{"_id":0,})
				for val in day_wise_find:
					if val["status"] == "IN":
						req["IN"].update({val['bus_no']:val['datetime']})

					elif val['status'] == "OUT":
						req["OUT"].update({val['bus_no']:val['datetime']})
				pubMessage = {"sender":"server","type":"resp","subType":"dayWiseStats","Message":req}
				mqttClient.publish(PUB_TOPIC,pubMessage)



	

	if (message["sender"] == "device"):
		if (message["type"] == "req"):
			if(message["subType"] == "busEntry"):
				if message["Message"]["card_no"] in bus_dic.keys():
					find_count = 0
					a=time.localtime(time.time())#forms a time_struc l
					r = a.tm_year
					t = a.tm_mon
					y = a.tm_mday
					b_num = bus_dic[message["Message"]["card_no"]]#GIVES A INTEGER VALUE FROM THE DICTIONARY					
					while(find_count==0):
						find_status = db.collection.find({"bus_no":b_num, "datetime":datetime.datetime(r, t, y)},{"_id":0,"status":1}).sort([("datetime" pymongo.DESCENDING)]).limit(1)#check status of the bus i.e, IN or OUT
						find_count = find_status.count()
						y-= 1
					for val in find_status:
						pass
					if val["status"] == "IN": #set status to "OUT" and insert
						d = db.collection.insert_one({"bus_No":b_num,"status":"OUT","datetime":datetime.datetime.now()}).inserted_id
						#DO DB INSERTION
					elif status =="OUT": #set status to "IN" and insert
						d = db.collection.insert_one({"bus_No":b_num,"status":"IN","datetime":datetime.datetime.now()}).inserted_id
						# do DB INSERTION 
'''
busEntry message format : message = {"sender":"device","type":"req","subType":"busEntry","Message":{"card_no":"<card_number>"}}
'''




'''
send message format : message = {
									"sender":"server",
									"type":"resp",
									"subType":"<type of request>"
									"message":{"<message_name>":"<message>"}
								}
'''
def mqttInit():
	# 1.3 Initializing mqtt client
	mqttClient = mqttPackage.Client()

	mqttClient.connect(hostname,port,timealive)

	mqttClient.on_connect = on_sub_connect
	mqttClient.on_message = on_message
	mqttClient.loop_start()
	mqttClient.loop_forever()


def dataPush():
	db.collection.insert_one(
        {
        "Bus_No":<Bus_number>,
        "Status":<Bus_status>,
        "Arrival_time":<time_of_arrival>, #time
        "Exit_time":<time_of_exit>
        })

def dataPull():
	colldata = db.collection.find()
    for data in colldata:
        print data


def dataUpdate():

	 db.collection.update_one(
        {<condtionkey: conditionval>},
        {
        "$set": {
            <updatekey>:<updateval>
        }
        }
        )
#------------------------------------------------------------------------------------
#     <find conditional>
#	All the methods below can be combined together
#------------------------------------------------------------------------------------
def search_between_days():			#search betwen 2 dates
	in_range = db.collection.find(
		{
		"datetime":{"$gte":<from_date>,"$lt":<to_date>}

		})
	for data in in_range:
		print data

def search_perticular_day():			#search no specific date
	in_range = db.collection.find(
		{
			"datetime":{"$lte":<to_date>}		
			#import datetime 
			#to_date, form_date = datetime.datetime(year, month, day)
			#format is mandatory

		})
	for data in in_range:
		print data


def retrieve_with_limit():				#limit retrieved data
	lmt = db.collection.find(<condition>).limit(<limit_condition>)
	#limit_condition should be an integer form range -2**31 to 2**31
	for data in in_range:
		print data


def req_field_only():
	fd = db.collection.find(<query>,<condition>)
	#query = {"desired condition"}
	#condition = {"field_1":1,"field_2":0}
	# 1 means retrieve
	# 0 means not

# def count_find():
# 	cnt = db.collection.find(<condition>).count()
# 	print count






if __name__ == '__main__':
	hostname  = 'iot.eclipse.org'
	port      = 1883
	timealive = 60
	SUB_TOPIC = "bT-card-req"


	mongo_conn = MongoClient('localhost:27017')

	db = mongo_conn.bus_track
	collection = db.bt_arr_dep_data

	mqttInit()




