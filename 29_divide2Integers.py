'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.
'''

from math import pow


def divide(dividend: int, divisor: int) -> int:
    cocient = dividend/divisor
    if cocient > pow(2,31)-1:
        return int(pow(2,31)-1)
    elif cocient < pow(-2,31):
        return int(pow(-2,31))
    else:
        return int(cocient)


# Pruebas

print(divide(dividend = 10, divisor = 3)) # Output -> 3

print(divide(dividend = 7, divisor = -3)) # Output -> -2

print(divide(dividend = -2147483648, divisor = -1)) # Output -> 2147483647