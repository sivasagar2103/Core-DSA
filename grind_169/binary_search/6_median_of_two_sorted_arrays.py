'''
Approach to the problem:
https://youtu.be/F9c7LpRZWVQ?si=eDGp8Wv_OvrH-oqf

1. Binary search on the smaller array to find the correct partition 
   where elements on the left are ≤ elements on the right.
* Partition
2. Total elements on the left = (n1 + n2 + 1) // 2
   (The extra "+1" handles both odd and even combined lengths)
* Binary Search Logic
3. Let mid1 be partition in arr1
4. Let mid2 = left - mid1 be partition in arr2
* Boundary Management:
6. If pointer is 0 or at end, skip accessing
* Valid Partition Condition:
7. if l1 <= r2 and l2 <= r1: (This ensures all left elements ≤ all right elements.)
8. Median Calculation:
* Binary Search Adjustments:
9. If l1 > r2 → too many elements from arr1, move left
10. Else → move right

Time complexity: O(log(min(n1, n2))
Space Complexity: O(1)

'''

def find_median_two_pointer(arr1, arr2):
    '''
    Time: O(n1 + n2) worst case
    Space: O(1)
    
    '''
    n1, n2 = len(arr1), len(arr2)
    total = n1 + n2
    i = j = 0
    prev = curr = 0
    
    #median indices
    mid = total // 2
    
    for k in range(mid + 1):
        prev = curr
        
        if i < n1 and (j >= n2 or arr1[i] <= arr2[j]):
            curr = arr1[i]
            i += 1
        else:
            curr = arr2[j]
            j += 1
    
    # odd total
    if total % 2 == 1:
        return curr
    else:
        return (prev + curr) / 2


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
