#Program to receive tag data and push to MongoDB

import pymongo
from pymongo import MongoClient

#create connection
try:
	client = MongoClient()
	print("Connection successfully!!")
except:
	print("Connection failed!!")
#connect to ip and port 
client = MongoClient('127.0.0.1', 27017)
#Access database
# database
try:
	db = client.sai
	print("Connected to database")
except:
	print("not connected")
 
# Created or Switched to collection names: seran
collection = db.seran
 
emp_rec1 = {
        "name":"Mr.Geek",
        "eid":24,
        "location":"delhi"
        }
emp_rec2 = {
        "name":"Mr.Shaurya",
        "eid":14,
        "location":"delhi"
        }
 
# Insert Data
rec_id1 = collection.insert_one(emp_rec1)
rec_id2 = collection.insert_one(emp_rec2)
 
print("Data inserted with record ids",rec_id1," ",rec_id2)
 
# Printing the data inserted
cursor = collection.find()
for record in cursor:
    print(record)