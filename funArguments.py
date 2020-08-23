def update(lst1):
    print(id(lst1))
    x= 8
    print(id(lst1))
    print("list 1" , lst1)

lst = [10,20,30]
print(id(lst))
update(lst)
print("list "  , lst)