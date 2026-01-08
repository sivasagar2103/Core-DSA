'''
Problem:
Given an integer array nums. Return the number of reverse pairs in the array.
An index pair (i, j) is called a reverse pair if:
0 <= i < j < nums.length
nums[i] > 2 * nums[j]

Approach:
1. Brute Force

Time: O(N**2)
Space: O(1)

2. Extended Merge Sort
Steps:
- Since both halves are sorted, you can quickly check for each left-element
  how many right-elements form a valid pair—no need to check every possible pair.
- Every count from the left and right halves gets added up along with the freshly
  calculated cross-pairs at each recursion level.

Time: O(NlogN)
Space: O(N)

'''



def count_pairs(arr, low, mid, high):
    print(arr)
    right = mid+1
    cnt = 0
    for i in range(low, mid+1):
        while right <= high and arr[i] > 2 * arr[right]:
            print(arr[i] , "and" ,  2 * arr[right])
            right += 1
        cnt += right - (mid + 1)
    return cnt

def merge_sort(arr, low, high):
    cnt = 0
    if low >= high:
        return cnt
    mid = (low + high)//2
    cnt += merge_sort(arr, low, mid) 
    cnt += merge_sort(arr, mid+1, high)
    cnt += count_pairs(arr, low, mid, high)
    merge(arr, low, mid, high)
    return cnt

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high+1):
        arr[i] = temp[i-low]

def count_reverse_pairs(arr):
    n = len(arr)
    result = merge_sort(arr, 0, n-1)
    return result


a = [4, 1, 2, 3, 1]
res = count_reverse_pairs(a)
print(res)