'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?
'''


def isPalindrome(x: int) -> bool:
    reverso = str(x) [::-1]

    return True if reverso == str(x) else False

# Pruebas
print(isPalindrome(121))            # Output ---> True

print(isPalindrome(-121))           # Output ---> False

print(isPalindrome(10))             # Output ---> False