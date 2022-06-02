'''
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

def strStr(haystack: str, needle: str) -> int:
    if len(needle) == 0:
        return 0
    elif needle in haystack:
        return haystack.index(needle)
    else:
        return -1


# Pruebas

print(strStr(haystack = "hello", needle = "ll")) # Output -> 2

print(strStr(haystack = "aaaaa", needle = "bba")) # Output -> -1