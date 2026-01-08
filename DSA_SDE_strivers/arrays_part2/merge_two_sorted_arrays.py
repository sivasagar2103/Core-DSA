'''
Problem:
Merge two sorted arrays without extra space

Approach:
1. Brute Force
Time: O()
Space:

2. Optimal Approach by using Gap Method
   - Initialize gap: (gap + 1) // 2
   - First Pass - A to A comparison: i > i+gap --> swap
   - Second Pass - A to B comparison: 
    * Cross-compare a[i] with b[j] when i + gap > len(a).
    * The index shift calculates i in a and j in b seamlessly.
   - Third Pass - B to B comparison: j > j+gap --> swap
   - Continue until gap becomes 0.

Time: O((n + m) log(n + m))
Space: O(1)

Note:
Intuition behind "gap":
- Think of the array as multiple sublists, each formed by elements at intervals of the gap.
- Each pass sorts these sublists via insertion or swap, improving local order.
- As the gap shrinks, these sublists expand and overlap until the final pass 
  with gap = 1 sorts the entire array efficiently.


'''
def merge_two_lists_bf(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    total = n1 + n2
    res = [0] * total
    index = 0
    left = 0
    right = 0

    while left < n1 and right < n2:
        if arr1[left] <= arr2[right]:
            res[index] = arr1[left]
            left += 1
            index += 1
        else:
            res[index] = arr2[right]
            right += 1
            index += 1
    
    while left < n1:
        res[index] = arr1[left]
        index += 1
        left += 1
    
    while right < n2:
        res[index] = arr2[right]
        index += 1
        right += 1


#Gap Method
def merge_two_lists(a, b):

    def find_gap(n):
        if n <= 1:
            return 0
        return (n+1)//2

    n1 = len(a)
    n2 = len(b)
    total = n1+n2
    gap = find_gap(total)

    while gap > 0:
        i = 0

        #compare a to a
        while i+gap < n1:
            if a[i] > a[i+gap]:
                a[i], a[i+gap] = a[i+gap], a[i]
            i += 1

        #compare a to b
        j = gap - n1 if gap > n1 else 0
        while i < n1 and j < n2:
            if a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
            i+=1
            j+=1
        
        #compare b to b
        j = 0
        while j+gap < n2:
            if b[j] > b[j+gap]:
                b[j], b[j+gap] = b[j+gap], b[j]
            j += 1
        
        gap = find_gap(gap)
    

nums1 = [-5, -2, 4, 5]
nums2 = [-3, 1, 8]
res = merge_two_lists(nums1, nums2)
print(nums1)
print(nums2)
