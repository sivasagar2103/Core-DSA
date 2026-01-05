'''
Approach to the Problem:
Instead of generating all n * m combinations (inefficient for large arrays),
we explore only promising candidates using a heap.

1. Sort Arrays (Descending):
Sorting both arrays ensures that the largest possible sum is at the top
(nums1[0] + nums2[0]), forming the starting point.
2. Max-Heap Usage:
A manually implemented max-heap is used to always extract the current largest
sum in O(log n) time.
3. Visited Set:
A set tracks index pairs (i, j) that are already processed to avoid duplicates in the heap.
4. Explore Next Combinations:
From any pair (i, j), only (i+1, j) and (i, j+1) are explored — these are the next
largest possible combinations.
5. Manual Heap Functions:
heap_push and heap_pop are built using heapify_up and heapify_down to maintain max-heap
structure without built-in methods.
6. Efficiency:
The solution ensures logarithmic heap operations and avoids unnecessary pair generation,
giving better than O(n²) performance.
7. Bug Prevention:
Carefully managing the visited set and indices ensures correct and non-redundant 
exploration of the search space.

Note: 
1. This algorithm smartly avoids generating all n * m combinations.
2. It leverages a max-heap to explore only the most promising pairs,
pushing at most 2k combinations and keeping time and space close to O(k log k) instead of O(n²).
3. Sorting helps set up the initial state, and the visited set prevents duplicates.

Time Complexity:

Sorting First Array: nlogn
Sorting Secondary Array: mlogm

Main Loop [k iterations]:
heap_pop and heapify : O(k log k)
heap_push at most 2 and heapify: O(2k log k)

Sorting Arrays - O(n log n + m log m)
Heap Operations - O(k log k)
Visited Set Ops - O(k)
Final Appends - O(k)

Total : O(n log n + m log m + k log k)

Space Complexity: O(k)

'''
#building max heap
def heapify_down(heap, root):
    maxi = root
    left = 2 * root  + 1
    right = 2 * root+ 1
    n = len(heap)
    
    if left < n and heap[left][0] > heap[maxi][0]:
        maxi = left
    if right < n and heap[right][0] > heap[maxi][0]:
        maxi = right
    
    if maxi != root:
        heap[maxi], heap[root] = heap[root], heap[maxi]
        heapify_down(heap, maxi)

def heap_pop(heap):
    top = heap[0]
    heap[0] = heap[-1]
    heapify_down(heap, 0)
    heap.pop()
    return top

def heapify_up(heap, index):
    parent = (index-1) //2
    if index > 0 and heap[index][0] > heap[parent][0]:
        heap[index], heap[parent] = heap[parent], heap[index]
        heapify_up(heap, parent)

def heap_push(heap, element):
    heap.append(element)
    heapify_up(heap, len(heap)-1)


def max_sum_combinations(nums1, nums2, k):
    nums1.sort(reverse = True)
    nums2.sort(reverse = True)

    max_heap = []
    visited = set()

    heap_push(max_heap, (nums1[0]+nums2[0], 0, 0))
    visited.add((0,0))

    result = []

    while k > 0 and max_heap:
        current_sum, i, j = heap_pop(max_heap)
        result.append(current_sum)
        k -= 1

        #i+1, j
        if i + 1 < len(nums1) and (i+1, j) not in visited:
            heap_push(max_heap, (nums1[i+1]+ nums2[j], i+1, j))
            visited.add((i+1, j))
        
        #i, j+1
        if i < len(nums1) and (i, j+1) not in visited:
            heap_push(max_heap, (nums1[i]+ nums2[j+1], i, j+1))
            visited.add((i, j+1))

    return result


nums1 = [7, 3]
nums2 = [1, 6]
k = 2
result = max_sum_combinations(nums1, nums2, k)
print(result)
