'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''

def lengthOfLastWord(s: str) -> int:
    sSplited = s.split(' ')
    sSplited.reverse()
    while len(sSplited[0]) == 0:
        sSplited.remove('')
    return len(sSplited[0])


print(lengthOfLastWord("Hello World"))      # Output -> 5

print(lengthOfLastWord("   fly me   to   the moon  "))      # Output -> 4

print(lengthOfLastWord("luffy is still joyboy"))      # Output -> 6