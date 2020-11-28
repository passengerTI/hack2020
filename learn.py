#!/usr/bin/python3

import random
from sklearn.linear_model import LinearRegression

# Create an empty list for the feature data set 'X' and the target data set 'y'
feature_set = []
target_set= []
# get the number of rows wanted for the data set
number_of_rows = 200
# limit the possible values in the data set
random_number_limit = 2000
#Create the training data set
#Create and append a randomly generated data set to the input and output
for i in range(0,number_of_rows):
  x = random.randint(0, random_number_limit)
  y = random.randint(0, random_number_limit)
  z = random.randint(0, random_number_limit)
  #Create a linear function for the target data set 'y'
  function = (10*x) + (2*y) + (3*z)
  feature_set.append([x,y,z])
  target_set.append(function)

model = LinearRegression() #Create a linear regression object/model
print(feature_set)
model.fit(feature_set, target_set) 

test_set = [[8,10,0]] 
prediction = model.predict(test_set)
print('Prediction:'+str(prediction)+'\t'+ 'Coefficient:'+str(model.coef_))