a = 10  #Global variable
print("global a",id(a))
def variables():
    a = 4    #local Variable
    #x = globals()['a']   # access the global variable with same in function
    #print("x",id(x))     #print id of accessed A variable
    print("Inside A:-",a)
    print(id(a))
    globals()['a']=15    #change global varable in function
variables()

print("Outside A:-",a)