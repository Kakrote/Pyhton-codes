class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def details(self):
        return f"name={self.name}\nroll no={self.roll}"
    @classmethod
    def from_str(cls,string):
        # param=string.split("-")
        # return cls(param[0],param[1])
        return cls(*string.split("-"))
Anshul=student.from_str("Anshul-13")
print(Anshul.details())  