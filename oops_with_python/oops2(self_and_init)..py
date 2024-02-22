class Student:
    def __init__(self,aname,aroll):
        self.name=aname
        self.roll=aroll
    def details(self): # self will take the argument a object on which this method is applied
        return f"name = {self.name}\nroll no = {self.roll}"
# s1=Student()
# s1.name="Anshul"
# s1.roll=13
# print(s1.details())
# s2=Student()
# s2.name="Neha Bisht"
# s2.roll=45
# print(s2.details())
s3=Student("muskan",42)
print(s3.details())