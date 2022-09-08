'''
Given a string s, return the longest palindromic substring in s.
'''

def longestPalindrome(s: str) -> str:
    x,y = 0,2
    long = ""
    while x < y <= len(s):
        while y <= len(s):
            out = s[x:y]
            rev = out[::-1]
            if out == rev and len(out) > len(long):
                long = out
            y += 1
        x += 1
        y = x+2
        
    return long
        


# Pruebas

print(longestPalindrome(s = "babad")) # Output -> "bab"

print(longestPalindrome(s = "cbbd")) # Output -> "bb"