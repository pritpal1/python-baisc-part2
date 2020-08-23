from numpy import *
arr1 = array([
                  [1,2,3,7],
                  [4,5,6,4]
    ])
#m = matrix(arr1)
#--------OR-----
m1 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')#way to create array using matrix ";" defines row nd col
m2 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
#m3= m1+m2
m3= m1*m2
print(m3)
#print(diagonal(m1))
#print(m1.max())
#print(m1.min())




