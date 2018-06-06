#Program to receive tag data and push to MongoDB
import pymongo
from file_parser_mongo import *
from pymongo import *
import time
class mongo_db:
	def __init__(self):
		pass

		'''
		Takes "db"=database_name, "collection"=collectio_name 
		as input "args" and connects to database and
		given collection.
		'''
	def mongo_connect(self,db,collection):
		try:
			print (host)
			self.conn = MongoClient(host)
			self.db = self.conn[db]
			self.db = self.db[collection]
			#print(self.conn)
			print(self.db)
			# self.collection_conn=
			# print(self.collection_conn)
			print('connected')
		except Exception as e:
			print(e)

		'''
		Takes a input as json, dict and inserts
		it into the database
		'''
	def mongo_insert(self,info):
		try:
			print (self.db)
			data=info
			self.insert=self.db.insert_one(data)
			print(self.insert)
		except Exception as e:
			print(e)
		'''
		This functin returns the timw stamp
		'''
	def time(self):
		self.a = time.localtime(time.time())
		if self.a.tm_hour >12:
			self.a.tm_hour=self.a.tm_hour-12
			print(self.a.tm_hour)
			pass
		self.t =[self.a.tm_hour]
		print(self.a.tm_hour)
		self.t.append(self.a.tm_min)
		self.t.append(self.a.tm_sec)
		self.v = '_'.join(str(e) for e in self.t)
		return self.v

	#def random_put(self):


				# #create connection
				# try:
				# 	client = MongoClient()
				# 	print("Connection successfully!!")
				# except:
				# 	print("Connection failed!!")
				# #connect to ip and port 
				# client = MongoClient(host)
				# #Access database
				# # database
				# try:
				# 	db = client.sai
				# 	print("Connected to database")
				# except:
				# 	print("not connected")
				 
				# # Created or Switched to collection names: seran
				# collection = db.seran
				 
				# emp_rec1 = {
				#         "name":"Mr.Geek",
				#         "eid":24,
				#         "location":"delhi"
				#         }
				# emp_rec2 = {
				#         "name":"Mr.Shaurya",
				#         "eid":14,
				#         "location":"delhi"
				#         }
				 
				# # Insert Data
				# rec_id1 = collection.insert_one(emp_rec1)
				# rec_id2 = collection.insert_one(emp_rec2)
				 
				# print("Data inserted with record ids",rec_id1," ",rec_id2)
				 
				# # Printing the data inserted
				# cursor = collection.find()
				# for record in cursor:
				#     print(record)