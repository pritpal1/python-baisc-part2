def count(lst):
    even = 0
    odd= 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst=[45,89,20,1,7,9,8,5]
even,odd =count(lst)
#print(even)
#print(odd)
print("Even: {} and Odd :{}".format(even,odd))