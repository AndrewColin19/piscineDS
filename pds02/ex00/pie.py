import matplotlib.pyplot as plt
import psycopg2

conn = psycopg2.connect(database="postgres",
                        user='postgres', password='mysecretpassword', 
                        host='127.0.0.1', port='5432'
)

cursor = conn.cursor()

sql = """SELECT event_type, count(*)
FROM customers WHERE event_type IS NOT null
group by event_type """

cursor.execute(sql)

resutl = cursor.fetchall()
labels = []
sizes = []
for t in resutl:
    labels.append(t[0])
    sizes.append(t[1])

fig1, ax1 = plt.subplots()

ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=180)

ax1.axis('equal')

plt.show()