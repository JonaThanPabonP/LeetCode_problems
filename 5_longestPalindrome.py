'''
Given a string s, return the longest palindromic substring in s.
'''

def longestPalindrome(s: str) -> str:
    longPalind = s[0]
    
    x,y = 0,2
    while x < y <= len(s):
        while y <= len(s):
            out = s[x:y]
            rev = out[::-1]
            if out == rev and len(out) > len(longPalind):
                longPalind = out
            y += 1
        x += 1
        y = x+2
            
    return longPalind


# Pruebas

print(longestPalindrome(s = "babad")) # Output -> "bab"

print(longestPalindrome(s = "cbbd")) # Output -> "bb"

print(longestPalindrome(s = "ab")) # Output -> "a"

print(longestPalindrome(s = "a")) # Output -> "a"