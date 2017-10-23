def createGenerator():
    myList = range(3)
    for i in myList:
        yield i*i



gen = createGenerator()
print(gen)

for g in gen:
    print(g)

for g in gen:
    print("hello", g)