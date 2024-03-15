import pickle
names=["Anshul","Rohit","Muskhan","neha"] # we have taken an exmple of list object but we could have use any other object.
file="pikecke.pkl"
f=open(file,"wb") # the file is save into binary formate and cant be opean in a gernal way .
pickle.dump(names,f)
f.close
f=open(file,"rb") # to read the fiel we have to opean it in a read binary formate 
read_names=pickle.load(f) # this load() un-pickle the pickle file. and convert it again in python object.
print(read_names)
f.close()