list2 = ["i","l","a","y"]
len_list2 = len(list2)


def four(mylist):
    for i,l in enumerate(mylist):
        if i%2==0:  
            print(i.upeer())
        else:
           print(i.lower())


four(mylist=list2)