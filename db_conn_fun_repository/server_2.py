import paho.mqtt.client as mqtt
import ast
import time as L
import datetime
from datetime import *
from pymongo import MongoClient
import json


#dictionary containing bus_numbers of respective card numbers
bus_dic = {4612:108,3452:215,1265:322,8760:223}

def on_connect(client, userdata, flags, rc ):
	print ("connected")
	(result,mid) = mqttClient.subscribe(SUB_TOPIC)


def on_message(client, userdata, msg):
	

	message = ast.literal_eval(msg.payload.decode("utf-8") )



	if (message["sender"] == "app"):
		if (message['type'] == "req"):
			if (message["subtype"] == "busCount"):
				#  do mongodb count get operation
				d = date.today()
				dt = datetime.combine(d, datetime.min.time())
				incount  = db.collection.find({"status":"IN", "datetime":{"$lt":dt}},{"bus_no":1,"_id":0}).count()
				outcount = db.collection.find({"status":"OUT", "datetime":{"$lt":dt}},{"bus_no":1,"_id":0}).count()

				pubMessage = {"sender":"server","type":"resp","subtype":"busCount","Message":{"inCount":incount,"outCount":outcount}}
				pubMessage = json.dumps(pubMessage)
				mqttClient.publish(PUB_TOPIC,pubMessage)
				L.sleep(5)

			


	


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
	hostname  = 'test.mosquitto.org'
	port      = 1883
	timealive = 60
	SUB_TOPIC = "bT-App"
	PUB_TOPIC = "bT-Server"


	mongo_conn = MongoClient('localhost:27017')

	db = mongo_conn.bus_track
	collection = db.bt_arr_dep_data

	mqttInit()




