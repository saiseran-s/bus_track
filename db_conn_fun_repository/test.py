import pymongo
from pymongo import *
import datetime

import time
# from time import *


client = MongoClient()
db = client.bus_track
collection=db.collection

b_num =108
r =2018
t= 7
y=2

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
			
# 			# req["OUT"].update({val['bus_no']:val['datetime']})


# except Exception as e:
# 	print(e)
req={"IN":{},"OUT":{}}

day_wise_find = db.collection.find({"datetime":{"$gte":datetime.datetime(r, t, y)}},{"_id":0,})
for val in day_wise_find:
	print(val)
	if val["status"] == "IN":
		req["IN"].update({val['bus_no']:val['datetime']})

	elif val['status'] == "OUT":
		req["OUT"].update({val['bus_no']:val['datetime']})
print(req)



# while(y):
# 	y=y-1
# 	if (y%2==0):
# 		time.sleep(300)
# 		l ="IN"
# 	else:
# 		time.sleep(30)
# 		l="OUT"
# 	d=db.collection.insert_one({"bus_no":b_num,"status":l,"datetime":datetime.datetime.now()})
# 	time.sleep(60)
	
