'''
About Heap:
- Heap is a specialised complete binary tree that satisfies heap property.
- All levels are fully filled , that too from left to right.
- Max Heap: each parent node is greater than or equal to its children. Max is at root.
- Min Heap: each parent node is smaller than or equal to its children. Min is at root.
Operations:
- Insert: O(logn) -- add node and restore heap - sift-up
- Extract Min/Max -- O(logn) -- remove and restore heap -- sift down
- Peek -- Access the min or max at the root in O(1) time.
- Heapify: convert an array into heap

About Building of Heap:
For array 'arr' of size n:
The last non-leaf node is at index n//2 - 1.
For each index i in reversed range n//2-1 to 0, apply sift-down.

Time Complexity: 
To build min and max heap: O(n)
Because most nodes are near the bottom and require much less work to heapify,
so the total sum of work done across all nodes is linear, not O(n log n)
"heapify" on a single node can take O(logn) time and there are n nodes.

Why Heaps Are Preferred for Complex Operations?
- Retrieve min/max in O(1) and insert/delete in O(log n),
  enabling highly efficient priority queue management.
- Handles changing datasets with rapid insertion, removal,
  or priority update, unlike sorted arrays or lists.

Build heap (bottom-up) : O(n)
Insert or remove (top): O(logn)
Get min/max: O(1)

'''

def max_heap(arr):
    n = len(arr)

    def heapify(root):
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        while left < n and arr[left] > arr[largest]:
            largest = left
        while right< n and arr[right] > arr[largest]:
            largest = right
        if largest != root:
            arr[root], arr[largest] = arr[largest], arr[root]
            heapify(largest)

    #n//2 - 1 -- last non leaf node
    for i in range(n//2-1, -1, -1):
        print(i)
        heapify(i)


def min_heap(nums):
    n = len(nums)

    def heapify(root):
        mini = root
        left = 2*root+1
        right = 2*root+2

        while left < n and  nums[left] < nums[mini]:
            mini = left
        while right < n and nums[right] < nums[mini]:
            mini = right

        if mini != root:
            nums[mini], nums[root] = nums[root], nums[mini]
            heapify(mini) 

    #heapify from the last non leaf node to 0
    for i in range(n//2-1, -1, -1):
        heapify(i)


#nums = [1, 2, 3, 4, 5]
nums = [5,4,3,2,1]
min_heap(nums)
print(nums)