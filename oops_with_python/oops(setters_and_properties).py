class anshul:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{self.fname}.{self.lname}@gmail.com"
    def print_names(self):
        return f"this is {self.fname} {self.lname}"
    def printemail(self):
        pass
# this is a function to chage the value of our email on runtime
    @property # this is our property decorater 
    def email(self):
        if self.fname==None or self.lname==None:
            return "no email is found sorry"
        return f"{self.fname}.{self.lname}@gamil.com"
    @email.setter # this is our setter
    def email(self,string):
        name=string.split("@")[0]
        self.fname=name.split(".")[0]
        self.lname=name.split(".")[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

    
a=anshul("anshul","pundir")
print(a.email)
a.fname="neha"
a.lname="bisth"
print(a.email)
a.email="rohit.rajput@gmail.com"        
print(a.fname)
print(a.email)
del a.email # will dete the email
print(a.email)
a.email="anshul.pundir@gmail.com" # will create a new email
print(a.email)