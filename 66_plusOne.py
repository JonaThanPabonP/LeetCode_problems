'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''

def plusOne(digits: list[int]) -> list[int]:
    if digits[-1] == 9:
        num = int("".join(map(str,digits)))
        num += 1
        digits = [int(i) for i in str(num)]
    else:
        digits[-1] += 1
    return digits


print(plusOne(digits = [1,2,3]))        # Output -> [1,2,4]

print(plusOne(digits = [4,3,2,1]))        # Output -> [4,3,2,2]

print(plusOne(digits = [9]))        # Output -> [1,0]