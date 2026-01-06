
#By Sorting
def kth_largest_element_by_sorting(arr, k):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


#By Heap
#In a min heap, the parent node must be less than or equal to its children.
def heapify(arr, i, size):
    '''
    making min heap

    '''
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

#heapify
def build_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, i, n)

def find_kth_largest_number_by_heap(arr, k):
    priority_arr = arr[:k]
    build_heap(priority_arr)

    for i in range(k, len(arr)):
        if arr[i] > priority_arr[0]:
            priority_arr[0] = arr[i]
            heapify(priority_arr, 0, k)

    return priority_arr[0]

#By quick select sort
def quick_select(arr, k):

    def partition(left, right, pivot_index):
        pivot_element = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left

        for i in range(left, right):
            if arr[i] > pivot_element:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        
        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index


    n = len(arr)
    left = 0
    right = n -1
    k_th_index = k -1

    while left <= right:
        pivot_index = left + (right - left) //2
        pivot_index = partition(left, right, pivot_index)

        if pivot_index == k_th_index:
            return arr[pivot_index]
        elif pivot_index < k_th_index:
            left = pivot_index + 1
        else:
            right = pivot_index - 1

nums = [3,2,1,5,6,4]
k = 4
#res = kth_largest_element_by_sorting(nums, k)
result = quick_select(nums, k)
print(result)
