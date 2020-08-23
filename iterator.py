#name=[2,3,4,5]
#it = iter(name)   #create name as itrator
#print(it.__next__()) #print
#print(next(it))

class Top10:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
values = Top10()
for i in values:
    print(i)

###generator with Yield
def topten():
    n =1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
obj=topten()
for i in obj:
    print(i)