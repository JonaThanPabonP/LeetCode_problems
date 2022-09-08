'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    newList = nums1 + nums2
    newList.sort()
    d = len(newList)
    if d%2 != 0:
        return newList[int(d/2)]
    else:
        return (newList[int(d/2)-1]+newList[int(d/2)])/2


# Pruebas

print(findMedianSortedArrays(nums1 = [1,3], nums2 = [2])) # Output -> 2.000

print(findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4])) # Output -> 2.5