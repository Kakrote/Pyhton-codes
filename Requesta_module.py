import os
import pickle
import json
os.chdir("c://")
f = open("C:\\Users\\anshu\\Downloads\\iris\\iris.data", "r")
reader = f.readlines()
# print(reader)
json_data=json.dumps(reader)
print(json_data)
f.close()
