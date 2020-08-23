from array import *
arr =array('i',[]) #creating empty arry
n = int(input("Enter lenght :- "))
for i in range(n):
    x = int(input("Enter next value  "))
    arr.append(x)

print(arr)

val = int(input("Enter  value for search  "))
#k=0
#for j in arr:
 #   if(j==val):
  #      print(k)
   #     break
    #k+=1



print(arr.index(val))

