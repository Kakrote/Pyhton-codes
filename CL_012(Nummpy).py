import pandas as pa # could be use to visualize the data provided 
import numpy as np
test=pa.read_csv('book.csv')
print(test.head()) # gives the top 5 datas
print(test.shape) # provide the data numbers accourdingly
print(test.describe()) # discribe the data in the tabuler form or the way it is describe in original file 
print(test.info()) # provide the information about the data avilable include properties of the data. it also give the info of the empty coloms.
test.isna().sum() # give the value is null or not 