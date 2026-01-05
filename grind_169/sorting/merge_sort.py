'''
Time: O(nlogn)
Space: O(n)

Merge Sort is a divide and conquers algorithm, it divides the given array
into equal parts and then merges the 2 sorted parts.

There are 2 main functions :
merge(): This function is used to merge the 2 halves of the array.
It assumes that both parts of the array are sorted and merges both of them.
mergeSort(): This function divides the array into 2 parts.
low to mid and mid+1 to high where,
low = leftmost index of the array
high = rightmost index of the array
mid = Middle index of the array

We recursively split the array, and go from top-down until
all sub-arrays size becomes 1.

'''

def merge(arr, low, mid, high):
    temp_arr  = []
    left = low
    right = mid+1

    while (left <= mid) and (right <= high):
        if arr[left] <= arr[right]:
            temp_arr.append(arr[left])
            left+=1
        else:
            temp_arr.append(arr[right])
            right+=1
    
    while left <= mid:
        temp_arr.append(arr[left])
        left+=1
    
    while right <= high:
        temp_arr.append(arr[right])
        right+=1
    
    for i in range(low, high+1):
        arr[i] = temp_arr[i-low]


#divides the array into parts until the size of the array is 1.
def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high)//2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)

arr = [12, 11, 13, 5, 6]
merge_sort(arr, 0, len(arr)-1)
print(arr)
