def function(*args_list):
    ans = []
    for l in args_list:
        ans.append(l.upper())

    return ans 

def function2(**kargs_list):
    ans = []
    for key , value in kargs_list.items():
        ans.append([key,value])
        
    return ans
    
object1 = function('python','function','tutorial')
print(object1)

object2 = function2(First = 'python', second = 'function', third = 'tutotial')
print(object2)