# this a code to explain the concept of set in the Python.
s=set([1,2,3,4])
print(type(s))
print(s)
list=[5,6,7,8] # this is a list 
s1=set(list) # we converted a list into a set.
print(type(s1))
# how to add in the set.
s1.add(2)
s1.add(3)
s1.add(4)
print(s1)
# we can perform all sets operation over the sets.
s1=s.union(s1) # we created a union of sets
print(s1)
s2=set([2,3])
s3=s2.intersection(s) # this is the intersecton of the two sets. 
print(s3)
