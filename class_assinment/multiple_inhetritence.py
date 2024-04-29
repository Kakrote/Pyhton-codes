details=['Neha bisht','MCA','B','45']
class Phone:
    def __init__(self,brand,modal):
        self.brand=brand
        self.modal=modal
    def call(self):
        print('calling....')

class Camera:
    def __init__(self,camera):
        self.camera=camera
    def cameraopean(self):
        print('opeaning camera.....')

class SmartPhone(Phone,Camera):
    def __init__(self, brand, modal):
        super().__init__(brand, modal) # calls the constructer of the Phone class 
        self.brand='Mi'
        Camera.__init__(self,self.brand) # calls the constructer of the Camera class
    def music(self):
        print('playing music....')

sm=SmartPhone("Nokia",5.1) # object for the SmartPhone class has been created 


#  calling all the functions of the parent class's using the object of the SmartPhone class
sm.call()
sm.cameraopean()
sm.music()

print(f'SmartPhone details= {sm.brand},{sm.modal},{sm.camera}\n')

for i in details:
    print(i)
