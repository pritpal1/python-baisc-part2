from numpy import *
arr1 = array([
                  [1,2,3,7,8,9],
                  [4,5,6,4,2,1]
    ])
print(arr1)
#print(arr1.dtype)
#print(arr1.ndim)
#print(arr1.shape) #it give the no of rows and cols
#print(arr1.size)  #size of entire array

#converting 2d array into 1d "Flatten()"
arr2 =arr1.flatten()
#print(arr2)

#converting 1d array into 2d"reshape(row,col)"
#arr3 = arr2.reshape(3,4)
arr3 = arr2.reshape(2,2,3) #one big arr : two 2d arr:2 single d array:3 values

print(arr3)