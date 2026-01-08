
'''
Approach:
1. Find the break-point, i: Break-point means the first index i from the back of
the given array where arr[i] becomes smaller than arr[i+1].
2. If a break-point exists
   - Find the smallest number i.e. > arr[i] and in the right half of index i
   (i.e. from index i+1 to n-1) and swap it with arr[i].
   - Reverse the entire right half(i.e. from index i+1 to n-1) of index i.
3. If such a break-point does not exist i.e. if the array is sorted in decreasing order,
the given permutation is the last one in the sorted order of all possible permutations. 
So, the next permutation must be the first i.e. the permutation in increasing order.
So, in this case, we will reverse the whole array

Time Complexity: O(3N), where N = size of the given array
Space Complexity: Since no extra storage is required. Thus, its space complexity is O(1).

'''

def next_permutation(arr):
    n = len(arr)
    i = n-2

    #finding the break point
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    
    #swap the first biggest number from the end compared to element at break point
    if i!=0:
        j = n-1
        while arr[j] <= arr[i]:
            j-=1
        arr[i], arr[j] = arr[j], arr[i]
    
    #Reverse the elements from i to n-1
    left = i+1
    right = n-1
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

arr = [2,1,5,4,3,0,0]
res = next_permutation(arr)
print(arr)
#Output: The next permutation is: [2 3 0 0 1 4 5 ]
