'''
Want Ascending Order:
Build Max heap and and place the largest element i.e.,root at its point at the end of
list and apply heapify property to satisfy the heap property of the disturbed node.

Want Descending Order:
Build Min heap and and place the smallest element i.e.,root at its point at the end of
list and apply heapify property to satisfy the heap property of the disturbed node.

Time complexity: 
Tobuildheap - O(n)
Each of the n-1 removals and heap rebalances - O(logn)
Total: O(nlogn)
Space Complexity: O(1)

'''


def heap_sort(nums):
    #convert the array into max heap
    n = len(nums)

    def heapify(root, size):
        mini = root
        left = 2 * mini + 1
        right = 2 * mini + 2

        while left < size and nums[left] > nums[mini]:
            mini = left
        while right < size and nums[right] > nums[mini]:
            mini = right
        if mini != root:
            nums[mini], nums[root] = nums[root], nums[mini]
            heapify(mini,size)

    #start form the non leaf node
    #bottom-up approach
    for i in range(n//2 -1, -1, -1):
        heapify(i, n)
    
    for j in range(n-1, 0, -1):
        nums[0], nums[j] = nums[j],nums[0]
        heapify(0, j)

    
arr = [64, 34, 25, 12, 22, 11, 90, 120]
heap_sort(arr)
print(arr)
