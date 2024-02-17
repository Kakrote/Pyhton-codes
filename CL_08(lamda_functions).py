# lamda are the one liner functions
add=lambda x,y:x+y
print(add(10,20))
list=[(1,2),(2,1),(3,3)]
print("befor the sorting of the list ",list)
# def list_(list):
#     return list[1]
# list.sort(key=list_)
print("After the sorting of the list ",list)
list2=["apple","cat","kiwi","Anshul","mukul"]
print("befor sorting of the list2 ",list2)
list2.sort(key=len) # sort the list accourding the len of the string in it
print("After the sorting of the list2 ",list2)
list.sort(key=lambda x:x[1])
print(list)