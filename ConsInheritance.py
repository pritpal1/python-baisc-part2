class A:
    def __init__(self):
        print("Init of A")

    def feature1(self):
        print("feature 1")


class B(A):   #B inherit A
    def __init__(self): #if u create obj of sub class it'll 1st try find init of sub class
        super().__init__()  #call init method of class A,
        print("Init of B")

    def feature2(self):
        print("feature 2")

b1 = B()
b1.feature1()

