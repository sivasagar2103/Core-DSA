'''

Intuition:
- Even though the array is rotated, one half is always sorted.
- Use that sorted half to decide whether to go left or right.

Core Idea:
- Pick mid.
- Check which side is sorted:
  . If arr[low] <= arr[mid] ⇒ left half sorted
  . Else ⇒ right half sorted
- Check if target lies within that sorted half:
  . If YES → move into the sorted half.
  . If NO → move into the other half.

Time: O(logn)
Space: O(n)

'''

def search_array(arr, target):
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == target:
            print(mid)
            return True
        
        elif arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid -1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid -1
    return False 


nums = [4,5,6,7,0,1,2]
target = 0
res = search_array(nums, target)
print(res)
