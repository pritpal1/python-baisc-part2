class A:
    def feature1(self):
        print("feature 1")
    def feature2(self):
        print("feature 2")

class B:   #B inherit A  #class B(A):
    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("feature 4")

class C(A,B):   #c inherit A,B multiple
    def feature5(self):
        print("feature 3")

    def feature6(self):
        print("feature 4")
c1 =C()
c1.feature2()
