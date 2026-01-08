'''
Approach to Solve the Problem:
1. Initialize two pointers:
   i for arr1, j for arr2
2. If one array is exhausted return the kth element of the next array since
    all are sorted.
3. If k == 1, return the smaller of current elements (arr1[i] and arr2[j])
4. Decide how many elements to compare in each array:
   - Take min between remaining elements and k // 2 → prevents overflow.
5. Compare the elements at those midpoints:
   - If arr1[i + mid - 1] < arr2[j + mid - 1], discard mid elements 
   from arr1 by moving pointer i
   - Else, discard mid from arr2 by moving pointer j
6. Reduce k by the number of elements you removed.
7. Repeat until k becomes 1, at which point you have narrowed it down to the answer.

Why min(len(arr) - pointer, k // 2)?
So you don't go out of bounds when fewer than k // 2 elements are left.
Keeps the algorithm safe and correct for arrays of different lengths.

Time Complexity: O(log k)
Space Complexity: O(log n)

'''

#union of two sorted arrays
def find_kth_element(arr1, arr2, k):
    i = j = 0
    while True:
        if i == len(arr1):
            return arr2[j + k - 1]
        if j == len(arr2):
            return arr1[i + k - 1]
        if k == 1:
            return min(arr1[i], arr2[j])
        
        '''
        Key logic to avoid going out of bounds
        We want to discard k // 2 elements each time (in binary search fashion).
        If there are fewer than k // 2 elements left in an array,
        we take what's available (len(arr1) - i or len(arr2) - j).

        '''
        mid1 = min(len(arr1) - i, k//2)
        mid2 = min(len(arr2) - j, k//2)

        '''
        Compare the two "k//2-th" elements of each array (from the current pointers).
        Whichever is smaller, the kth element cannot be in the first k//2 elements 
        of that array, because we've just confirmed that they are smaller.
        So, we advance the pointer in that array by mid_arrX, effectively 
        eliminating those elements from consideration, 
        and decrease k to reflect this.
        
        '''

        if arr1[i + mid1 - 1] < arr2[j + mid2 - 1]:
            i += mid1
            k -= mid1
        else:
            j += mid2
            k -= mid2


a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
res = find_kth_element(a, b, k)
print(res)