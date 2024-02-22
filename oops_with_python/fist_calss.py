class Students:
    no_of_leaves=9 # this is a class variable
s1=Students()
s2=Students()
s1.name="Anshul pundir"
s1.roll_no=13
s2.name="Rohit"
s2.roll_no=58
print(s1.name)
print(s1.no_of_leaves)
print(s2.no_of_leaves)
s2.no_of_leaves=10 # this is a istence variable
s1.no_of_leaves=11 # this is a istence variable
print(s1.no_of_leaves)
print(s2.no_of_leaves)
print(Students.__dict__) # before the change in class variable
Students.no_of_leaves=20 # this will make change in class variable
print(Students.__dict__) # after the change in class variable