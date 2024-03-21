# sam sharma 
# hello dear student.
class person:
    def __init__(self,fname,lname):
        self.fname=fname # these are class variables
        self.lname=lname
    def show(self):
        print(self.fname,self.lname)
class student(person):
    def msg(self):
        print(self.fname,self.lname,"hellow dear student")
std=student("Anshul","Pundir")
# std.show()
std.msg()
        