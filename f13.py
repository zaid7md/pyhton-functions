def new(l):
    a = []
    for i in l:
        if i not in a:
            a.append(i)

    print(a)

list = [1 , 1,  1 , 1 ,2 , 3, 4 ,5 ,5 ]
new(list)