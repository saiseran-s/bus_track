import MySQLdb
from file_parser import *
import time

class sql_db:
	def __init__(self):
		pass
#
#
	def sql_conn(self):
		try:
			self.conn = MySQLdb.connect(host,usr,pwd,database)
			print("DB connected!!")
			time.sleep(1)

		except Exception as e:
			print(e)
			print("Error in connecting to DB")
		try:
			self.cur = self.conn.cursor()
			print("Cursor active!")
			time.sleep(1)
		except Exception as e:
			print(e)
			print("Cursor failed")
#Note: This function should only be executed once at the begining
#This function is to create a new table

	def sql_create_table(self,table_name,col1,col2,tab1,tab2):
		sql = "CREATE TABLE " + table_name + " AS (" + "SELECT "
		col1 = col1.split(',')
		col2 = col2.split(',')
		for i in col1:
			sql = sql + tab1+"."+i+","
		for j in col2:
			sql = sql + tab2+"."+j+","
		sql = sql.rstrip(',') + ") FROM " + tab1 +", "+ tab2+" WHERE "
		print(sql)

#
#
#
	def sql_insert(self,table_name,col,val):
		try:
			sql = "INSERT INTO " + table_name + "("
			for i in range(len(col)):
				sql = sql + col[i]
			sql = sql + ")" + "values("
			for i in range(len(val)):
				sql = sql + val[i]
			sql = sql + ");"
			print(sql)
			self.cur = self.conn.cursor()
			self.cur.execute(sql)
		except Exception as e:
				print (e)
#
#
#	def sql_update(self,table_name,col,val):
	def db_date(self):
		a = time.localtime(time.time())
		t =[a.tm_mday]
		t.append(a.tm_mon)
		t.append(a.tm_year)
		v = '_'.join(str(e) for e in t)
		return v
