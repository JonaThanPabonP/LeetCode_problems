'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.
'''

def removeElement(nums: list[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1

    return nums, len(nums)

# Pruebas

print(removeElement(nums = [3,2,2,3], val = 3)) # Output -> 2 - nums = [2,2,_,_]

print(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)) # Output -> 5 - nums = [0,1,4,0,3,_,_,_]