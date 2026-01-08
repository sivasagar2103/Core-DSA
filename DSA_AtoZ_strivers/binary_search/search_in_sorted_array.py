'''
Approach to Solve the Problem:
1. The algorithm extends binary search to handle rotated arrays 
    by identifying which half of the array is sorted at every step.
2. Each iteration, you check if the target is equal to the middle element.
3. If not, determine which side (left or right) is sorted:
    - If the left part (arr[low] to arr[mid]) is sorted,
      check if k is in this range. If so, adjust high to mid-1
      otherwise search in the right.
    - If the right part (arr[mid] to arr[right]) is sorted,
      check if k is in this range. If so, adjust low to mid+1
      otherwise search in the left.
4. This continues until we found the element or search space runs out.

Why this approach?
1. It maintains the essence of binary search.
2. It avoids linear scan.
3. No need to preprocess of sorting the array.

Time Complexity: O(log n)
Sapce Complexity: O(1)

'''

def find_element(arr, k):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            return mid
        
        if arr[low] <= arr[mid]:
            if arr[low] <= k < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < k <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1

'''
Approach to Solve the Problem:
1. The function uses a modified binary search to efficiently find the pivot.
2. It maintains two pointers: low and high at the ends of the array.
3. In each iteration:
   - calculates the middle index mid.
   - compares arr[mid] with arr[high].
   - If arr[mid] is greater than arr[high],
     it means the smallest element is in the right half
     (pivot is to the right), so low is updated to mid + 1.
    - Otherwise, the smallest element is in the left half 
      or could be mid itself, so high is updated to mid.
    - This process continues until low == high, at which 
      pointlow points to the pivot index.

Time Complexity: O(log n)
Space Complexity: O(1)

'''

def find_pivot(arr):
    n = len(arr)
    low = 0
    high = n-1

    while low < high:
        mid = (low +high) //2

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return low                              


nums = [4, 5, 6, 7, 0, 1, 2]
k = 0
res = find_element(nums, k)
print(f"{k} is at : {res}")
pivot = find_pivot(nums)
print(f"pivot is at {pivot}")