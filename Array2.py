from numpy import  *
arr1 = array([1,2,3,4,5])
arr2 = array([11,12,13,14,15])
arr3 = arr1+arr2 #add 2 array()vectorized operation
#print(arr3)
#arr1= arr1+5  #add 5 in all elements
#print(sqrt(arr1))
#print(sum(arr1))
#print(min(arr1))
#print(max(arr1))
#print(concatenate([arr1,arr2]))
#arr4 = arr1.view() #creat 2 array with same value,shallow copy make in both array
arr4 = arr1.copy() #deep copy
arr1[1]=9 #changing arrays value
print(arr1)
print(arr4)
print(id(arr1))
print(id(arr4))
print(arr1)



