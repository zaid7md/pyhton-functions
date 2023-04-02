#perfect number 
def perfect(a):
    sum = 0
    for i in range(1,a):
        if(a%i==0):
            sum+=i

    return(sum==n)


n = int(input("Enter number "))
print(perfect(n))