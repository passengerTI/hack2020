#!/usr/bin/python3

from sklearn.linear_model import LinearRegression
import pymysql
import math

db = pymysql.connect("localhost","hack2020","simple7Start","hack2020")

def laern_gipertenziya():
  ### START learn gipertenziya
  cursor = db.cursor()
  cursor.execute("SELECT working, pension,work_end_by_ill,diabet,diabet_long FROM sovershen1 WHERE arterial_gipper = 1")
  summ = cursor.fetchone()
  print(summ)

  feature_set = []
  target_set = []

  # Set default
  summ_elements = 5

  cursor.execute("SELECT working, pension,work_end_by_ill,diabet,diabet_long FROM sovershen1 WHERE arterial_gipper = 1")
  rows = cursor.fetchall()


  for row in rows:
    # Set summ in real life
    summ_elements = len(row)
    # Prepare
    kernel = (1*row[0]) + (1*row[1]) + (1*row[2]) + (1*row[3]) + (1*row[4])
    feature_set.append([row[0],row[1],row[2],row[3],row[4]])
    target_set.append(kernel)

  model = LinearRegression()
  model.fit(feature_set, target_set)

  test_set = [[1,1,0,0,1]]
  prediction = model.predict(test_set)

  percent = 5/float(prediction)*100

  print("Percent: " + str(percent))
  print('Prediction:'+str(prediction)+'\t'+' Coefficient'+str(model.coef_))
  ### END learn gipertenziya
  return 1

def laern_onmk():
  ### START learn gipertenziya
  cursor = db.cursor()
  cursor.execute("SELECT working, pension,work_end_by_ill,diabet,diabet_long FROM sovershen1 WHERE onmk = 1")
  summ = cursor.fetchone()
  print(summ)

  feature_set = []
  target_set = []

  summ_elements = 5

  cursor.execute("SELECT working, pension,work_end_by_ill,diabet,diabet_long FROM sovershen1 WHERE onmk = 1")
  rows = cursor.fetchall()

  for row in rows:
    kernel = (1*row[0]) + (1*row[1]) + (1*row[2]) + (1*row[3]) + (1*row[4])
    feature_set.append([row[0],row[1],row[2],row[3],row[4]])
    target_set.append(kernel)

  model = LinearRegression()
  model.fit(feature_set, target_set)

  test_set = [[1,1,0,0,1]]
  prediction = model.predict(test_set)

  percent = 5/float(prediction)*100

  print("Percent: " + str(percent))
  print('Prediction:'+str(prediction)+'\t'+' Coefficient'+str(model.coef_))
  ### END learn gipertenziya
  return 1

def laern_infarkt():
  ### START learn gipertenziya
  cursor = db.cursor()
  cursor.execute("SELECT working, pension,work_end_by_ill,diabet,diabet_long FROM sovershen1 WHERE infarkt = 1")
  summ = cursor.fetchone()
  print(summ)

  feature_set = []
  target_set = []

  summ_elements = 5

  cursor.execute("SELECT working, pension,work_end_by_ill,diabet,diabet_long FROM sovershen1 WHERE infarkt = 1")
  rows = cursor.fetchall()

  for row in rows:
    kernel = (1*row[0]) + (1*row[1]) + (1*row[2]) + (1*row[3]) + (1*row[4])
    feature_set.append([row[0],row[1],row[2],row[3],row[4]])
    target_set.append(kernel)

  model = LinearRegression()
  model.fit(feature_set, target_set)

  test_set = [[1,1,0,0,1]]
  prediction = model.predict(test_set)

  percent = 5/float(prediction)*100

  print("Percent: " + str(percent))
  print('Prediction:'+str(prediction)+'\t'+' Coefficient'+str(model.coef_))
  ### END learn gipertenziya
  return 1

def laern_heart_failure():
  ### START learn gipertenziya
  cursor = db.cursor()
  cursor.execute("SELECT working, pension,work_end_by_ill,diabet,diabet_long FROM sovershen1 WHERE heart_failure = 1")
  summ = cursor.fetchone()
  print(summ)

  feature_set = []
  target_set = []

  summ_elements = 5

  cursor.execute("SELECT working, pension,work_end_by_ill,diabet,diabet_long FROM sovershen1 WHERE heart_failure = 1")
  rows = cursor.fetchall()

  for row in rows:
    kernel = (1*row[0]) + (1*row[1]) + (1*row[2]) + (1*row[3]) + (1*row[4])
    feature_set.append([row[0],row[1],row[2],row[3],row[4]])
    target_set.append(kernel)

  model = LinearRegression()
  model.fit(feature_set, target_set)

  test_set = [[1,1,0,0,1]]
  prediction = model.predict(test_set)

  percent = 5/float(prediction)*100

  print("Percent: " + str(percent))
  print('Prediction:'+str(prediction)+'\t'+' Coefficient'+str(model.coef_))
  ### END learn gipertenziya
  return 1

def laern_otherill():
  ### START learn gipertenziya
  cursor = db.cursor()
  cursor.execute("SELECT working, pension,work_end_by_ill,diabet,diabet_long FROM sovershen1 WHERE other_ill = 1")
  summ = cursor.fetchone()
  print(summ)

  feature_set = []
  target_set = []

  summ_elements = 5

  cursor.execute("SELECT working, pension,work_end_by_ill,diabet,diabet_long FROM sovershen1 WHERE other_ill = 1")
  rows = cursor.fetchall()

  for row in rows:
    kernel = (1*row[0]) + (1*row[1]) + (1*row[2]) + (1*row[3]) + (1*row[4])
    feature_set.append([row[0],row[1],row[2],row[3],row[4]])
    target_set.append(kernel)

  model = LinearRegression()
  model.fit(feature_set, target_set)

  test_set = [[1,1,0,0,1]]
  prediction = model.predict(test_set)

  percent = 5/float(prediction)*100

  print("Percent: " + str(percent))
  print('Prediction:'+str(prediction)+'\t'+' Coefficient'+str(model.coef_))
  ### END learn gipertenziya
  return 1

### Run un function

learn_gipertenziya()
laern_onmk()
laern_infarkt()
laern_heart_failure()
laern_other_ill()


db.close()