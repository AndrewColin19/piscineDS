import psycopg2

conn = psycopg2.connect(database="postgres",
                        user='postgres', password='mysecretpassword',
                        host='127.0.0.1', port='5432')

conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE temp (LIKE customers);
        INSERT INTO temp SELECT DISTINCT ON (event_type, product_id, price, user_id, user_session)* FROM customers;
        DROP TABLE customers;
        ALTER TABLE temp RENAME TO customers;'''

cursor.execute(sql)

conn.close()