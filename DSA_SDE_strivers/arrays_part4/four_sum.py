'''
Problem:
Given an integer array nums and an integer target.
Return all quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
- a, b, c, d are all distinct valid indices of nums.
- nums[a] + nums[b] + nums[c] + nums[d] == target.

Approach:
* Sorting and Two Pointer
- Sort the array first -- O(nlogn)
- Fix one element at a time [i = 0]
- Fix second element at a time [j = 1]
- Two pointers for the remaining part [left = j+1, right = n-1]
- Adjust pointers based on sum:  -- 
    nums[i] + nums[j] + nums[left] + nums[right] == target -- valid -- left+1, right-1
    nums[i] + nums[j] + nums[left] + nums[right] < target -- left+1
    nums[i] + nums[j] + nums[left] + nums[right] > target -- right-1
- skip duplicates over i, j, left and right

Time: O(N**3), where N = size of the array.
Space: O(k) -- k is the no of quadruplets

'''

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid +1

    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= mid:
        temp.append(arr[left])
        left +=1
    
    while right <= high:
        temp.append(arr[right])
        right +=1
    
    for i in range(low, high + 1):
        arr[i] = temp[i-low]

def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high)//2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)


def four_sum(arr, target):
    res = []
    n = len(arr)
    merge_sort(arr, 0, n-1)

    for i in range(n):

        if i != 0 and arr[i] == arr[i-1]:
            continue

        for j in range(i+1, n):

            if j > i+1 and arr[j] == arr[j-1]:
                continue
            
            k = j+1
            l = n-1

            while k < l:
                total = arr[i] + arr[j] + arr[k] + arr[l]
                if total < target:
                    k += 1
                elif total > target:
                    l -= 1
                else:
                    res.append([arr[i], arr[j], arr[k], arr[l]])
                    k += 1
                    l -= 1

                    while k < l and arr[k] == arr[k-1]:
                        k+=1
                    while k < l and arr[l] == arr[l+1]:
                        l -= 1
    return res



nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
target = 9
result = four_sum(nums, target)
print(result)
#The quadruplets are: [1 1 3 4 ] [1 2 2 4 ] [1 2 3 3 ]