'''
Problem:
Given an integer array sorted in non-decreasing order, remove the duplicates 
in place such that each unique element appears only once. The relative order 
of the elements should be kept the same.

Approach:
1. Two Pointer Approach


Time: O(N)
Space: O(1)

'''


def remove_duplicates(arr):
    n = len(arr)
    i = 0
    j = 1

    while j < n:
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
        j+=1
    
    return i + 1


arr = [1,1,2,2,2,3,3]
res = remove_duplicates(arr)
print(res)
