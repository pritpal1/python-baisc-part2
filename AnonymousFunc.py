from functools import reduce
f= lambda a:a*a
result = f(5)
print(result)

# another use of lambda with Filter(),reduce(),map()
nums = [2,7,8,4,6,5,1]
evens = list(filter(lambda n:n%2==0,nums))
print("Filter even numbers:-",evens)
doubles = list(map(lambda n:n*2,nums))
print("Find doubles of even numbers:-",doubles)
sum = reduce(lambda a,b:a+b,doubles)
print("sum of doubles num:-",sum)