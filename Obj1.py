class Computer:

    def __init__(self,cpu,ram):    #call automatically
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is",self.cpu,self.ram)

com1=Computer('i5',16) #creating object
com2 =Computer('i3',8)
#Computer.config(com1) #calling method 1st
com1.config()  #calling method 2nd
com2.config()