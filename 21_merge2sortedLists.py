'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''



def mergeTwoLists(list1: list[int], list2: list[int]) -> list[int]:
    result = list1+list2
    result.sort()
    return result


# Pruebas

print(mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4])) # Output -> [1,1,2,3,4,4]

print(mergeTwoLists(list1 = [], list2 = [])) # Output -> []

print(mergeTwoLists(list1 = [], list2 = [0])) # Output -> [0]