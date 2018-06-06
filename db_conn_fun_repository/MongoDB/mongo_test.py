from mongo_conn import *
from file_parser_mongo import *

c = mongo_db()
datab=db
collection=collection
c.mongo_connect(datab,collection)
seran = input("enter")
anisha =c.time()
print(anisha)
# raj = input('Enter your email-id')
info={
	"bus_is":bus_id,
	"time":anisha,
	# "email_id":raj
}
c.mongo_insert(info)

