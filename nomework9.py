def m(number):
    mylist = []
    for i in range(number):
        if i % 2 == 0 and i % 3 == 0:
            mylist.append(i)
    return mylist
x = m(20)
print(x)



#for i in range(80):
#    print(i % 2)

