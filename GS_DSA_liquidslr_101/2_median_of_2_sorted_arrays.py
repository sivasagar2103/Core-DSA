'''
Problem Statement:
Given two sorted arrays arr1 and arr2, find the median of the 
combined sorted array without actually merging them.

Approach Used: Binary Search on the Smaller Array

Core Idea:
- Split both arrays into left and right partitions
- Ensure: max(left part) ≤ min(right part)
- The left partition should contain half of the total elements
- Always Binary Search on the Smaller Array (len(arr1) < len(arr2))

Time: O(log(min(n1, n2)))
Space: O(1)

'''


def find_median(arr1, arr2):
    if len(arr2) < len(arr1):
        arr1, arr2 = arr2, arr1
    n1 = len(arr1) #3
    n2 = len(arr2) #
    total = n1 + n2

    left = (total + 1) // 2 #added 1 for handling odd
    low = 0
    high = n1

    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1

        l1, l2 = float('-inf'), float('-inf')
        r1, r2 = float('inf'), float('inf')

        if mid1 < n1:
            r1 = arr1[mid1]
        if mid2 < n2:
            r2 = arr2[mid2]
        if mid1-1 >= 0:
            l1 = arr1[mid1-1]
        if mid2-1 >= 0:
            l2 = arr2[mid2-1]

        #Left part is sorted
        if l1 <= r2 and l2 <= r1:
            if total%2 == 1:
                return max(l1, l2)
            else:
                maxi = max(l1, l2)
                mini = min(r1, r2)
                return (maxi + mini)//2
        
        if l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    
    return 0


arr1 = [2, 4, 6]
arr2 = [1, 3, 5,7, 8, 9, 10,11]
res = find_median(arr1, arr2)
print(res)
