'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

def twoSum(nums, target):
    suma = 0
    for i in range(len(nums)):
        for n in range( i+1, len(nums)):
            suma = nums[i] + nums[n]
            if suma == target:      # Compara que la suma coincida con el número objetivo.
                return [i,n]

# Pruebas

print(twoSum([2,7,11,15], 9))       # Output -> [0,1]

print(twoSum([3,2,4], 6))       # Output -> [1,2]

print(twoSum([3,3], 6))       # Output -> [0,1]