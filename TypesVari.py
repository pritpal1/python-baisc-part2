class Car:
    wheels = 4  #class variables
    def __init__(self):   #instance variable
        self.mil = 10
        self.com ="BWM"

c1 = Car()
c2 = Car()
c2.mil = 12     #change instance variable
Car.wheels = 2   #change in class variable can change
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)