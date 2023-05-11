import matplotlib.pyplot as plt
import psycopg2
import numpy as np
from decimal import Decimal

connec = psycopg2.connect(database="postgres",
                        user='postgres', password='mysecretpassword', 
                        host='127.0.0.1', port='5432'
)

sql_nbCustomers = """SELECT count(*) as nb_customers, to_char(date(event_time),'YYYY-MM-dd') as date_time
FROM customers WHERE event_type = 'purchase'
group by date_time"""

sql_priceall = """SELECT SUM(price) AS allprice, CAST(event_time AS varchar(7)) AS MonthDay
FROM customers WHERE event_type = 'purchase'
GROUP BY MonthDay"""

result = None
result1 = None

with connec as conn:
    with conn.cursor() as curs:
        curs.execute(sql_nbCustomers)
        result = curs.fetchall()
        curs.execute(sql_priceall)
        result1 = curs.fetchall()

x, y, x1, y1, x2, y2 = [], [], [], [], [], []

for row in result:
    y.append(row[0])
    x.append(np.datetime64(row[1]))

fig, ax = plt.subplots()

ax.plot(x, y, lw=1)
ax.set_ylabel('Number of Customers')
ax.label_outer()
ax.grid(True)
ax.set_xlim([x[0], x[len(x) - 1]])


fig1, ax1 = plt.subplots()
for row in result1:
    y1.append(int(float(("".join(d for d in row[0] if d.isdigit() or d == '.')))))
    x1.append(np.datetime64(row[1]))
print(y1)
print(x1)
ax1.bar(x=x1, y=y1, height=1000000)

plt.xticks([np.datetime64("2022-10-01"), np.datetime64("2022-11-01"), np.datetime64("2022-12-01"), np.datetime64("2023-01-01")], labels=["oct", "nov", "dec", "jan"])
plt.show()

