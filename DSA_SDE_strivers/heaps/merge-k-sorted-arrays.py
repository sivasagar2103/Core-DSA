'''

Core Idea:
- Use a min-heap to always extract the smallest unmerged element from the front of the arrays.
- At any point, the heap contains the next smallest candidate from each array.

Approach:
- Initialize an empty min-heap.
- Push the first element of each array into the heap (along with array and index info).
- While heap is not empty:
  . Pop the smallest item and add it to the result.
  . Push the next element from the same array (if it exists).
- Repeat until all elements are merged.

Time:
Total elements = k * k = n
Each element is pushed and popped from the heap once → O(k²)
Heap size is at most k → O(log k) per operation
Total = O(k² log k)

Space:
Min-heap holds up to k elements → O(k)
Output array stores all elements → O(k²)
Total space = O(k²)

Why this?
- Maintains a heap of size k, avoids full re-sorting.
- Heap gives us the next global minimum efficiently.

'''
def heapify_up(heap, index):
    parent = (index-1)//2
    if parent >= 0 and heap[parent][0] > heap[index][0]:
        heap[parent], heap[index] = heap[index], heap[parent]
        heapify_up(heap, parent)

def heap_push(heap, element):
    heap.append(element)
    heapify_up(heap, len(heap)-1)

def heap_pop(heap):
    if not heap:
        return
    if len(heap) == 1:
        return heap.pop()
    top = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    heapify_down(heap, 0)
    return top

def heapify_down(heap, index):
    mini = index
    left = 2*index+1
    right = 2*index+2
    size = len(heap)

    if left < size and heap[left][0] < heap[mini][0]:
        mini = left
    if right < size and heap[right][0] < heap[mini][0]:
        mini = right
    if mini != index:
        heap[mini], heap[index] = heap[index], heap[mini]
        heapify_down(heap, mini)
    

def merge_arrays(matrix):
    k = len(matrix)
    heap = []
    result = []

    for i in range(k):
        if matrix[i]:
            heap_push(heap, (matrix[i][0], i, 0))
    
    while heap:
        current, arr_idx, element_idx = heap_pop(heap)
        result.append(current)

        if element_idx+1 < len(matrix[arr_idx]):
            next_val = matrix[arr_idx][element_idx+1]
            heap_push(heap, (next_val, arr_idx, element_idx+1))
    
    return result


arr = [[1,2,3],[4,5,6],[7,8,9]]
res = merge_arrays(arr)
print(res)
