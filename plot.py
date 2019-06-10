import sqlite3
import io
import numpy as np
import matplotlib.pyplot as plt




conn = sqlite3.connect('base_datos3.db')
c = conn.cursor()
wordUsed = 'Python Sentiment'
sql = "SELECT Peso, Fecha FROM Pesos WHERE Id = 1"

time = []
peso = []

c.execute(sql)

records = c.fetchall()



for row in records:
    peso.append(row[0])
    time.append(row[1])


fig = plt.figure()
rect = fig.patch
ax1 = fig.add_subplot(1,1,1, axisbg='white')
plt.plot_date(x=time, y=peso, fmt='b-', label = 'value', linewidth=2)
plt.show()   

