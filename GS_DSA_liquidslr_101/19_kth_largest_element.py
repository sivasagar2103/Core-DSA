'''
Problem Statement:
Given an integer array arr and an integer k,
return the kth largest element in the array.

Approach Used: Max Heap (Heap Sort Logic)

Core Idea:
A max heap always keeps the largest element at the root
Repeatedly removing the root simulates sorting from largest to smallest
After k-1 removals, the root is the kth largest

Time: O(n+klogn)
Space: O(1)

Quickselect → average O(n)
Heap is preferred when:
Streaming data
You need multiple kth queries

'''

def find_kth_largest_element(arr, k):
    n = len(arr)

    def heapify(i, size):
        maxi = i
        left = 2*i+1
        right = 2*i+2

        if left < size and arr[left] > arr[maxi]:
            maxi = left
        if right < size and arr[right] > arr[maxi]:
            maxi = right
        
        if maxi != i:
            arr[maxi], arr[i] = arr[i], arr[maxi]
            heapify(maxi, size)

    #converting array to heap
    parent = n//2 -1
    for i in range(parent, -1, -1):
        heapify(i, n)


    #swapping the root and last. Then heapify
    for i in range(n-1, n-k, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(0, i)
    
    return arr[0]



nums = [1, 2, 3, 4, 5]
k = 3
res = find_kth_largest_element(nums, k)
print(nums)
print(res)