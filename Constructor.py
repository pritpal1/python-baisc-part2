class Computer:

    def __init__(self):
        self.name = "prit"
        self.age = 21

    #def update(self):
         #self.age=31
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()

if c1.compare(c2):
    print("same")
else:
    print("different")

c2.name = "pritpal"
print(c1.name,c1.age)
print(c2.name)
#c2.update()
#print(c2.age)