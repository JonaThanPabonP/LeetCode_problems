'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''


def runningSum(nums: list[int]) -> list[int]:
    out = [nums[0]]

    for i in range(len(nums)-1):
        out.append(out[i] + nums[i+1])

    return out

# Pruebas

print(runningSum(nums = [1,2,3,4])) # Output -> [1,3,6,10]

print(runningSum(nums = [1,1,1,1,1])) # Output -> [1,2,3,4,5]

print(runningSum(nums = [3,1,2,10,1])) # Output -> [3,4,6,16,17]