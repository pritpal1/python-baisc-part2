#import sys
#sys.setrecursionlimit(20) #set limit of recursion
#print(sys.getrecursionlimit())
def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)

result = fact(int(input("Enter value:-")))
print(result)


