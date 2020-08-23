from array import *
#delete array
val = array('i',[5,8,9,4,7])
for i in val:
    if i==9:
        continue
    print(i)

#reverse array
val1 = array("i",[3,4,5,7,1])
print(val1[::-1]) #slicing [start:end:jump]
val2 = array("i",[])
for e in range(1,6):
    val2.append(val1[-e])
print(val2)



