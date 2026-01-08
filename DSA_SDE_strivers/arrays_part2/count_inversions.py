'''
Problem:
Given an array of N integers, count the inversion of the array
What is an inversion of an array? 
Definition: for all i & j < size of array, if i < j then you have to 
find pair (A[i],A[j]) such that A[j] < A[i].

Approach:
Divide: Recursively split the array into halves, like Merge Sort.
Conquer: Count inversions in: Left half, Right half, While merging both halves
Merge:
Compare elements from left and right subarrays.
When arr[left] <= arr[right], append and move left.
When arr[left] > arr[right], increment the inversion count by (mid - left + 1)
because all remaining elements from left to mid are greater.
Append elements and rebuild the sorted array.

Time: O(n log n)
Space: O(n)

'''

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    count = 0

    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            #increment the inversion count by (mid - left + 1)
            # because all remaining elements from left to mid are greater.
            count += (mid - left) + 1
            right += 1
    
    while left <= mid:
        temp.append(arr[left])
        left+=1
    
    while right <= high:
        temp.append(arr[right])
        right+=1
    
    for i in range(low, high + 1):
        arr[i] = temp[i-low]
    
    return count


def merge_sort(arr, low, high):
    count = 0
    if low >= high:
        return count
    mid = (low + high) // 2
    count += merge_sort(arr, low, mid)
    count += merge_sort(arr, mid+1, high)
    count += merge(arr, low, mid, high)
    return count


def count_inversions(arr):
    n = len(arr)
    return merge_sort(arr, 0, n-1)



a = [5, 4, 3, 2, 1]
res = count_inversions(a)
print(res)
