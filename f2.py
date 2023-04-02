def exp(a,b):
    return a**b

a = int(input("Enter no. : "))
b = int(input("Enter power : "))

print("%d^%d ="%(a,b),exp(a,b))


def merge_list(l1 , l2):
    l3 = l1 + l2 
    return l3 

list1 = [1 , 2 , 3 , 4,  5]
list2 = [6,67,87,6]
list3 = merge_list(list1,list2)
print("Merged list : ",list3)