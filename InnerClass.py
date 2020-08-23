class student:
    def  __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def show(self):
        print(self.name,self.rollno)

    class Laptop:       #inner class
        def __init__(self):
            self.brand ="HP"
            self.cpu ='i5'
            self.ram = 8
        def show(self):
            print(self.brand)

s1=student('prit',2)
s1.show()
lap1 = student.Laptop()  #creating obj of inner class
lap1.show()
