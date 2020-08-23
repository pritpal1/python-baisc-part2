#def person(name,age=15):    #default
def person(name,age):
    print("name is:" ,name)
    print("Age:" ,age)
person("prit",28)             #position
#person(age=28,name="prit")   #keyword
#person('prit')                #default value

#variable length
#def sum (a,*b):   #int a + tuple b
def sum (*b):
    #c=a   c contain "a" int
    c=0
    for i in b:
        c = c+i
    print(c)
sum(5,6,5)