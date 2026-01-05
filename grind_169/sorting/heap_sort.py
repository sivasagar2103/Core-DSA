'''
Convert array to max heap = O(n)
Extract max repeatedly = O(nlogn)
Total = O(nlogn)

Time : O(nlogn)
Space : O(1)

Max heap → ascending sort (largest to the end).
1. Start from the last non-leaf node [n // 2 - 1].
2. Heapify each node[i] up to the root (in reverse level order)
3. Call heapify(arr, i, n) to make the subtree rooted at i a max heap.
4. Extract Elements and Sort
5. Repeat for i from n-1 to 1
6. Swap the root (arr[0], max value) with arr[i]
7. Reduce heap size by 1 (i.e., heapify(arr, 0, i)).
8. Restore the max heap property by heapifying from the root.

Min heap → descending sort (smallest to the end).

'''


def heap_sort(arr):

    #To ensure the heap property
    def heapify(arr, i, size):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < size and arr[left] < arr[smallest]:
            smallest = left
        if right < size and arr[right] < arr[smallest]:
            smallest = right
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            heapify(arr, smallest, size) 


    #converting the array into heap
    n = len(arr)
    parent = n//2-1
    for i in range(parent, -1, -1):
        heapify(arr, i, n)

    #swaping root and and last node. Then heapify to maintain order
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)



arr = [64, 34, 25, 12, 22, 11, 90, 120]
heap_sort(arr)
print(arr)
