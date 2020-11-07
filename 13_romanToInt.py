'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

def romanToInt(s: str) -> int:
    romanNumbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romanSpecialNumbers = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    suma = 0
    i, j = 0, 1 
    while i in range(len(s)):
        
        while j <= len(s):
            temp = int(romanNumbers[s[i]])
            if j == len(s):
                suma += temp
                i += 1
                break

            if temp < int(romanNumbers[s[j]]) :
                specialNumber = s[i]+s[j]
                suma += romanSpecialNumbers[specialNumber]
                i += 2
                                
            else:
                suma += temp
                i += 1
            
            j = i+1

    return suma

# Pruebas
print(romanToInt('III'))        # Output ---> 3

print(romanToInt('IV'))         # Output ---> 4

print(romanToInt('IX'))         # Output ---> 9

print(romanToInt('LVIII'))      # Output ---> 58

print(romanToInt('MCMXCIV'))    # Output ---> 1994