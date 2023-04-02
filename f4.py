def sqaure(l1):
    sq = []
    for i in l1:
        sq.append(i**2)
    return(sq)

l = []
a = int(input("Enter the size of list : "))
for j in range(a):
    c = int(input("Enter element : "))
    l.append(c)
print("Original list",l)
print("Sqaure of elements int the list : ",sqaure(l))