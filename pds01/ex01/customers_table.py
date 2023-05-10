import psycopg2

conn = psycopg2.connect(database="postgres",
                        user='postgres', password='mysecretpassword',
                        host='127.0.0.1', port='5432')

conn.autocommit = True
cursor = conn.cursor()

cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
tables = cursor.fetchall()

names = []
for table in tables:
    if (table[0].startswith("data_202")):
        names.append("SELECT * FROM " + table[0])

sql = f"CREATE TABLE IF NOT EXISTS customers AS ({' UNION '.join(names)})"
cursor.execute(sql)

conn.close()