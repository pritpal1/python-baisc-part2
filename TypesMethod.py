class Student:
    uni = "sbbs"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1 + self.m2+self.m3)/3
    @classmethod
    def info(cls):      #working with class methode instead of passing Self pass "cls"
        return cls.uni

    @staticmethod
    def static1():
        print("This is static method of class Student")

    def get_m1(self):
        return self.m1
    def set_m1(self,value):
         self.m1 = value

s1 = Student(23,45,67)
print(s1.avg())   #calling instance method
print(Student.info())      #calling class method
Student.static1()          #calling static method
#s1.set_m1(2)   passing value to set_m1
#print(s1.get_m1())
