'''
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

def reverse(x):

    arr = []
    arr_rev = []
    x_abs = abs(x)
    x_str = str(x_abs)
    

    for i in x_str:
        arr.append(i)
    

    for j in range(len(arr)-1, -1, -1):  
        arr_rev.append(arr[j])
    

    if arr_rev[0] == "0":
        arr_rev.pop(0)

    rev = 0    
    for i in arr_rev:
        rev = int("".join(arr_rev))


    if x < 0 and rev*-1 >= -(2**31):
        return(rev*-1)
    elif x >= 0 and rev <= (2**31)-1:
        return(rev)
    else:
        return(0)


# Pruebas

print(reverse(123))         # Output ---> 321

print(reverse(-123))         # Output ---> -321

print(reverse(120))         # Output ---> 21