import pymongo
from pymongo import *
import datetime
# from datetime import *

from datetime import datetime
from datetime import *

# import time
# from time import *


client = MongoClient()
db = client.bus_track
collection=db.collection

b_num =108
r =2018
t= 7
y=13

d = datetime(2018, 7, 14)

# req={b_num:[[]]}

# req = {b_num:{"log":[],"OUT":[]}}

# day_wise_find = db.collection.find({"datetime":{"$gte":datetime(2018, 7, 14)}},{"_id":0,})
# req = {}
# for v in day_wise_find:
# 	req.update({v["bus_no"]:[]})

# print (req)
# day_wise_find = db.collection.find({"datetime":{"$gte":datetime(2018, 7, 14)}},{"_id":0,})

# for val in day_wise_find:
	
# 	req[val["bus_no"]].append([val["status"],str(val["datetime"])])


# 	# 
# 	# if val["status"] == "IN":
# 		# req["IN"].update({val['bus_no']:val['datetime']})
# 	# req[b_num]["IN"].append(val['datetime'])
# 	# req[val["bus_no"]].append([val["status"],val["datetime"]])

# print (req)

# 	# elif val['status'] == "OUT":
	# 	req["OUT"].update({val['bus_no']:val['datetime']})
# pubMessage = {"sender":"server","type":"resp","subType":"dayWiseStats","Message":req}
# pubMessage = json.dumps(pubMessage)
# mqttClient.publish(PUB_TOPIC,pubMessage)


# dt = datetime.combine(d, datetime.min.time())
# print(dt)
# incount  = db.collection.find({"status":"IN", "datetime":{"$lt":dt}},{"bus_no":1,"_id":0}).distinct("bus_no")

# outcount = db.collection.find({"status":"OUT", "datetime":{"$lt":dt}},{"bus_no":1,"_id":0}).distinct("bus_no")
# print (incount)
# print(outcount)
# bus_wise_find = db.collection.find({"datetime":datetime.datetime(r, t, y)},{"_id":0, "bus_no":1,"datetime":1,"status":1}).sort("datetime", pymongo.ASCENDING).limit(20)
# req = {b_num:{"IN":[],"OUT":[]}}
# try:
# 	find_status = db.collection.find({"bus_no":b_num},{"_id":0}).sort("datetime", pymongo.DESCENDING).limit(20)
# 	for val in find_status:
		
# 		if val["status"] == "IN":
# 			req[b_num]["IN"].append(val['datetime'])	

# 			# req["IN"].update({val['bus_no']:val['datetime']})

# 		elif val['status'] == "OUT":
# 			req[b_num]["OUT"].append(val['datetime'])
			
# 			#req["OUT"].update({val['bus_no']:val['datetime']})


# except Exception as e:
# 	print(e)
# req={"IN":{},"OUT":{}}

# day_wise_find = db.collection.find({"datetime":{"$gte":datetime.datetime(r, t, y)}},{"_id":0,})
# for val in day_wise_find:
# 	print(val)
# 	if val["status"] == "IN":
# 		req["IN"].update({val['bus_no']:val['datetime']})

# 	elif val['status'] == "OUT":
# 		req["OUT"].update({val['bus_no']:val['datetime']})
# print(req)



# while(y):
# 	y=y-1
# 	if (y%2==0):
# 		time.sleep(300)
# 		l ="IN"
# 	else:
# 		time.sleep(30)
# 		l="OUT"
# t = datetime.datetime.now()
# print(t)
# reddy = db.col2.find({"bus_no":b_num, "datetime":{"$gt":datetime.datetime(r, t, y )}}).count()

# # for r in reddy:
# print(reddy)
# if reddy == 0:
# 	saireddy = db.col2.insert_one({"bus_no":b_num,"status":	"OUT","datetime":datetime.datetime.now()}).inserted_id
# 	print(saireddy)
# 	for val in saireddy:
# 		print(val)

# elif reddy >= 1:
# 	saireddy = db.col2.find_one_and_update({"bus_no":b_num,"status":"OUT","datetime":{"$gt":datetime.datetime(r, t, y)}},{"$set":{"status":"IN", "datetime":datetime.datetime.now()}}, upsert=True)

# 	print(saireddy)
# d=db.col2.find_one_and_update({"bus_no":b_num,"status":"IN","datetime": {'$gte':datetime.datetime(r, t, y, 11, 24)}},{ '$set': {"status":"OUT", "datetime":datetime.datetime.now() }}, upsert=True)
# for f in d:
# 	print(f)

s="14.07.2018.12"
da = (int, s.split('.'))
D=int(da[1][0])
M=int(da[1][1])
Y=int(da[1][2])
H=int(da[1][3])
if (int(da[1][4]) == NULL):
	Min = 0
else:
	Min=int(da[1][4])

try:
	pass
except Exception as e:
	raise
else:
	pass
finally:
	pass
print("year",Y,"month", M,"say", D, "Hour",H,"Min", Min)