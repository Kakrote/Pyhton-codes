class A:
    def __init__(self):
        self.name='anshul'
class B(A):
    def __init__(self):
        super().__init__() # now this will give the call to the constructer of the super class and find the instence there
        self.roll=13
        self.name="Aman" # b.name will give the Aman as output as 
        super().__init__() # it enters again in the super class cunstrurert now the output would be the Aman

b=B()
print(b.name) # as there is no such istence in the construter of the class we have the instence already there 


