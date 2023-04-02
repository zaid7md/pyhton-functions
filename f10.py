def sum(list):
    sum = 0 
    for i in list:
        sum = sum + i 

    return(sum)

list = [1,2,3,4,5,6]
a = sum(list)
print("Sum of list :",a)