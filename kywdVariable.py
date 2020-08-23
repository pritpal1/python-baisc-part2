def person(name,**data):
    print(name)
    #print(data)
    for i,j in data.items():
        print(i,j)
person("prit",Age=21,City="Adampur")