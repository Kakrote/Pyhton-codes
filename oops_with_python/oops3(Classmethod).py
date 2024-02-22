class Students:
    @classmethod
    def change(cls,new_leves):
        cls.no_of_leaves=new_leves
        return cls.no_of_leaves
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
s2.change(32) # this is a class method and will make change directly into the class variable not in instence variable
print(Students.no_of_leaves)
print(Students.__dict__)