def palindrome(num):
    c = num 
    s = 0 
    while(num > 0):
        r = num%10
        s = s*10 + r
        num = num//10

    print("Reversed number :",s)
    if(s==c):
        print("Number is palindrome")
    else:
        print("Number is not palindrome")

a = int(input("ENTER NUMBER : "))
palindrome(a)