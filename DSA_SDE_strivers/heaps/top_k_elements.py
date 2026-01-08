'''
Problem:
Given an integer array nums and an integer k, 
return any order list of the k most frequent elements in nums.

Approach:
- Count frequencies of all elements using a dictionary.
- Initialize a min-heap (size at most K).
- For each (element, frequency):
  . Push (frequency, element) into the heap.
  . If heap size exceeds K, pop the smallest.
- The heap now contains the top K elements by frequency.
- Extract elements from the heap and return them.

Time:
Build frequency map: O(n)
heap_push: O(log k)
heap_pop: O(log k)
Final list creation: O(k)
Total: O(nlogk)

Space:
Frequency dictionary: O(n)
Heap (size limited to k): O(k)
Result list: O(k)
Total: O(n)

Note: We can solve by using both min heap and max heap.
But,
Min-heap is more efficient when k is small, because you maintain only k elements
in the heap.
Max-heap is simpler by storing all n items and k is not tiny.
Both use O(n) space due to the frequency dictionary.

'''

def array_frequency(arr):
    freq = {}
    for num in arr:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
    return freq

def heapify_up(heap, index):
    #building min heap
    parent = (index-1)//2
    if parent >= 0 and heap[parent][0] > heap[index][0]:
        heap[parent], heap[index] = heap[index], heap[parent]
        heapify_up(heap, parent)

def heap_push(heap, element):
    heap.append(element)
    heapify_up(heap, len(heap)-1)

def heapify_down(heap, index):
    n = len(heap)
    mini = index
    left = 2*index+1
    right = 2*index+2

    if left < n and heap[left] < heap[mini]:
        mini = left
    if right < n and heap[right] < heap[mini]:
        mini = right
    if mini != index:
        heap[mini], heap[index] = heap[index], heap[mini]
        heapify_down(heap, mini)

def heap_pop(heap):
    if not heap:
        return
    if len(heap) == 1:
        return heap.pop()
    heap[0] = heap.pop()
    heapify_down(heap, 0)
    
    
def top_k_elements(arr, k):
    freq_dict = array_frequency(arr)
    heap = []

    for key, value in freq_dict.items():
        heap_push(heap, (value, key))
        if len(heap) > k:
            heap_pop(heap)
    
    return [num for freq, num in heap]


nums = [1,1,1,2,2,3,3,3,3]
k = 2
res = top_k_elements(nums, k)
print(res)