def reverse(a):
    s = ""
    for i in range(1,len(a)+1):
        s = s +a[-i] 

    return s

a = input("Enter string : ")
print("Reversed : ",reverse(a))