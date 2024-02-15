List1=["Anshul","Rohit","Ayush","Vivek singh",30,10,20]
# to print the list
print(List1) 
# to print the indivisual items of the list we can use the indexing method as well
print(List1[3])# to print the item in the index value of 3.
#using a loop is also a method to print the items of the list one by one.
for l in List1:
    print(l)
# now lets talk about the slicing in the elements in the list.
numbers=[1,2,3,4,5,6,7,87,89,343,5654,]
numbers.sort()
numbers.reverse()
print(numbers)
print(numbers[:6])# it includes the index value of 0 by defult 
print(numbers[2:8])#it excludes the the value of 8 as it start from 2 and goes upto the 8-1 i.e 7.
print(numbers[0:100])#no matter what is the limit it will autometicaly adjust it to the size of the list.