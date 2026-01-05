'''
Sliding Window Maximum

Core Idea:
For every window of size k, efficiently track the maximum element
while the window slides one step at a time.

Brute force is O(nk), so we optimize using Heap or Deque.

Approach 1: Max Heap (Priority Queue)
Intuition
Store elements along with their indices in a heap.
The heap always keeps the maximum element at the top.
Remove elements that fall out of the window.

Steps of implementation:
1. Initialize an empty max heap.
2. Traverse the array:
    . Push (-value, index) into the heap.
3. Once the window reaches size k:
    Remove elements whose index is out of the window.
    The heap top gives the maximum for the current window.
4. Append the maximum to the result list.
5. Continue until all windows are processed.

Why use negative numbers in heapq?
- Python's heapq implements a min-heap only. There is no built-in max-heap.
- Negate the values. The largest original value becomes the smallest negative value.

Time: O(n log n)
Space: O(n)
(Slightly slower due to heap cleanup.)

Approach 2: Monotonic Deque
Intuition
Maintain a deque where elements are stored in decreasing order.
The front of the deque always holds the maximum of the window.
Remove:
    Elements smaller than current (they will never be max)
    Elements that fall out of the window
Steps of implementation:
1. Initialize an empty deque to store indices.
2. Traverse the array:
    Remove indices from the back whose values are smaller than current.
    Add current index to the deque.
    Remove the front index if it is outside the window.
3. Once window size reaches k:
    Append the value at the front of the deque to the result.
4. Return the result list.

Time: O(n)
Space: O(k)

'''
import heapq

def maximum_subarray(arr, k):
    n = len(arr)
    res = []
    max_heap = []  # (-value, index)

    for i in range(n):
        heapq.heappush(max_heap, (-arr[i], i))

        # Remove elements outside window
        while max_heap[0][1] <= i - k:
            heapq.heappop(max_heap)

        if i >= k - 1:
            res.append(-max_heap[0][0])

    return res

from collections import deque

def maximum_subarray_two(arr, k):
    n = len(arr)
    res = []
    dq = deque()  # stores indices

    for i in range(n):
        # Remove smaller elements from the back
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        # Remove elements outside window
        if dq[0] <= i - k:
            dq.popleft()

        # Add result once window size reaches k
        if i >= k - 1:
            res.append(arr[dq[0]])

    return res


nums = [1,3,-1,-3,5,3,6,7]
k = 3

res1 = maximum_subarray(nums, k)
print(res1)

res2 = maximum_subarray_two(nums, k)
print(res2)
