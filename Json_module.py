import json
data='{"var1":"anshul","var2":"pundir"}'
print("type of data before")
print(type(data))  # the type of data is string write now
parse=json.loads(data) # the loads() function parse the data into python dict 
print("after parsing of the data ")
print(type(parse)) # the data is now converted into the dict of python

# converting a python object to the json object.
dic={
    "roll_no":1,
    "name":"Anshul pundir",
    "class":"MCA II(B)",
}
print("befor the converting into the json object")
print(type(dic))
#  converting into the json object now
json_obj=json.dumps(dic)
print("After converting into the json object")
print(type(json_obj))

# writting into the json file 
dic2={
    "name":"Anshul Pundir",
    "class":"BBA",
    "p.no":7505316239
}
print("writng into the json file")
# opeaning file pointer
f1=open("tryfile.json","+a")
json.dump(dic2,f1)
f1.close()