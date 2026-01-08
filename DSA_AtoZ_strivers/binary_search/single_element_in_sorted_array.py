'''
To find the single element in a sorted array 
where every other element appears exactly twice, 
except for one unique element.

'''

def find_single_element(arr):
    n = len(arr)
    low = 0
    high = n - 1

    while low < high:

        mid = (low + high) // 2

        if mid % 2 == 1:
            mid -= 1

        if arr[mid] == arr[mid + 1]:
            low = mid + 2
        
        else:
            high = mid

    if low < n and (
        low == 0 or arr[low] != arr[low-1]) and (
            low == n - 1 or arr[low] != arr[low +1]):
        return arr[low]

    return -1



nums = [1,1,2,3,3,4,4,8,8]
res = find_single_element(nums)
print(res)