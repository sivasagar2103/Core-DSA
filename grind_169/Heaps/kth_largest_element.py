'''
Max-heap full + extract
Time Complexity: O(n + klogn)
Space Complecity: O(1)

Quickselect:
Time Complexity: O(n) avg; O(n²) worst
Space Complecity: O(1) avg; O(log n) recursion

Min-heap size k:
Time Complexity: O(n log k)
Space Complecity: O(k)

'''
def find_kth_largest_element(arr, k):
    n = len(arr)

    def heapify(root, size):
        #max heap
        maxi = root
        left = 2 * root + 1
        right = 2 * root +2

        if left < size and arr[left] > arr[maxi]:
            maxi = left
        if right < size and arr[right] > arr[maxi]:
            maxi = right
        
        if root != maxi:
            arr[root], arr[maxi] = arr[maxi], arr[root]
            heapify(maxi, size)


    for i in range(n//2-1, -1, -1):
        heapify(i, n)
    
    #start, stop, step
    for j in range(n-1, n-k, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify(0, j)
    
    return nums[0]

nums = [1, 2, 3, 4, 5]
k = 2
res = find_kth_largest_element(nums, k)
print(nums)
print(res)