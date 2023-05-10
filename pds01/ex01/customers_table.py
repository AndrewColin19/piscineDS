import psycopg2
import os

conn = psycopg2.connect(database="postgres",
                        user='postgres', password='mysecretpassword', 
                        host='127.0.0.1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql = f'''CREATE TABLE IF NOT EXISTS customers (
    event_time timestamp with time zone,
    event_type VARCHAR (50),
    product_id INTEGER,
    price MONEY,
    user_id numeric,
    user_session text
    );'''

cursor.execute(sql)
allTable = ""
	
for filename in os.listdir(os.getcwd() + "/customer"):
	#with open(os.path.join(os.getcwd() + "/customer/" , filename), 'r') as f: # open in readonly mode
	allTable = allTable + " " + filename[:len(filename) - 4]

sql = f'''Select * into customer  from  {allTable}'''
cursor.execute(sql)
conn.close()