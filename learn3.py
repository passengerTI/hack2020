#!/usr/bin/python3

from sklearn.linear_model import LinearRegression
import pymysql
import math

db = pymysql.connect("localhost","hack2020","simple7Start","hack2020")

cursor = db.cursor()
cursor.execute("SELECT working, pension,work_end_by_ill,diabet,diabet_long FROM sovershen1 WHERE arterial_gipper = 1")
summ = cursor.fetchone()
print(summ)

feature_set = []
target_set = []

summ_elements = 5

cursor.execute("SELECT working, pension,work_end_by_ill,diabet,diabet_long FROM sovershen1 WHERE arterial_gipper = 1")
rows = cursor.fetchall()

for row in rows:
  kernel = (1*row[0]) + (1*row[1]) + (1*row[2]) + (1*row[3]) + (1*row[4])
  feature_set.append([row[0],row[1],row[2],row[3],row[4]])
  target_set.append(kernel)

model = LinearRegression()
model.fit(feature_set, target_set)

test_set = [[1,1,0,0,1]]
prediction = model.predict(test_set)

percent = float(prediction)/5

print("Percent: " + str(percent))
print('Prediction:'+str(prediction)+'\t'+' Coefficient'+str(model.coef_))




db.close()