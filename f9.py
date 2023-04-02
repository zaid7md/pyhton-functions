def max(a,b,c):
    if(a>b and a>c):
        print(a,"is the largest")
    elif(b>c and b>a):
        print(b,"is the largest")
    else:
        print(c , "is the largest")

a = int(input('enter number 1 : '))
b = int(input('enter number 1 : '))
c = int(input('enter number 1 : '))

max(a,b,c)