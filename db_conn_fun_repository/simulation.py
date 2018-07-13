import paho.mqtt.client as mqtt
import ast
import time
import datetime
import json


def on_connect(client, userdata, flags, rc ):
	print ("connected")
	(result,mid) = mqttClient.subscribe(SUB_TOPIC)


def on_message(client, userdata, msg):
	print(msg.keys())
	message = ast.literal_eval(msg.payload)

def mqttInit():
	# 1.3 Initializing mqtt client
	global mqttClient
	mqttClient = mqtt.Client()

	mqttClient.connect(hostname,port,timealive)

	# mqttClient.on_connect = on_connect
	# mqttClient.on_message = on_message
	# mqttClient.loop_start()
	# mqttClient.loop_forever()

if __name__ == '__main__':
	hostname  = 'localhost'
	port      = 1883
	timealive = 60
	PUB_TOPIC = "bT-Server"
	SUB_TOPIC = "bT-App"

	mqttInit()



	r = int(input("1. Count stats\n2. Day wise stats\n3. Bus Wise stats\n4. Enter bus number\n"))

	if r == 1:
		message = {"sender":"app","type":"req","subtype":"busCount"}
		message = json.dumps(message)
		mqttClient.publish(PUB_TOPIC, message)
		time.sleep(5)
		print(message)

	elif r == 2:
		message = {"sender":"app","type":"req","subtype":"dayWiseStats","Date":"2018-07-12"}
		message = json.dumps(message)
		mqttClient.publish(PUB_TOPIC, message)
		# time.sleep(5)
		print(message)
	elif r == 3:
		message = {"sender":"app","type":"req","subtype":"busWiseStats","bus_number":108}
		message = json.dumps(message)
		mqttClient.publish(PUB_TOPIC, message)
		# time.sleep(5)
		print(message)
	elif r == 4:
		message = {"sender":"device","type":"req","subtype":"busEntry","Message":{"card_no":4612}}
		message = json.dumps(message)
		mqttClient.publish(PUB_TOPIC, message)
		time.sleep(5)
		print(message)