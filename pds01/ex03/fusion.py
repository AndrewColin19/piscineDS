import psycopg2

conn = psycopg2.connect(database="postgres",
                        user='postgres', password='mysecretpassword',
                        host='127.0.0.1', port='5432')

conn.autocommit = True
cursor = conn.cursor()

sql = '''ALTER TABLE customers
	ADD IF NOT EXISTS category_id text,
    ADD IF NOT EXISTS category_code varchar(50),
    ADD IF NOT EXISTS brand text;
    INSERT INTO customers (product_id, category_id, category_code, brand) SELECT * FROM items'''
    
cursor.execute(sql)

conn.close()