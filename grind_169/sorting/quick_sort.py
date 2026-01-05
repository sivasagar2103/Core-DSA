'''

Time: O(nlogn)
Space: O(1) + O(N) auxiliary stack space.

Quick Sort is a divide-and-conquer algorithm like the Merge Sort. 
But unlike Merge sort, this algorithm does not use any extra array 
for sorting(though it uses an auxiliary stack space).
So, from that perspective, Quick sort is slightly better than Merge sort.

Pick a pivot and place it in its correct place in the sorted array.
Shift smaller elements on the left of the pivot and larger ones to the right.

The main intention of this process is to place the pivot, 
after each recursion call, at its final position, 
where the pivot should be in the final sorted array.

'''


def parition_index(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while i <= high and arr[i] <= pivot:
            i+=1
        while j >= low and arr[j] > pivot:
            j-=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low, high):
    if low < high:
        #to choose pivot as middle element
        #pivot_index = (low + (high - low))//2
        #arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
        p_index = parition_index(arr, low, high)
        quick_sort(arr, low, p_index-1)
        quick_sort(arr, p_index+1, high)


arr = [12, 11, 13, 5, 6]
quick_sort(arr, 0, len(arr)-1)
print(arr)