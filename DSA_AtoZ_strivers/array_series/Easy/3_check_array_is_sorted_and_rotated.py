
'''
- A sorted + rotated array will have at most one point 
  where the order breaks (descending step).
- That point marks the rotation index.
- If there's more than one break, the array isn't sorted-rotated.

- count : tracks the violations of sorted order.
  rotation_index : stores the index where the rotation happens.
- modulo (% n) ensures the last element is compared with the first one (circular check).
- count > 1, means the elements are not sorted after the first finding.

'''

def check(arr):
    count = 0
    rotation_index = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[(i+1) % n]:
            count += 1
            rotation_index = (i+1)%n
        if count > 1:
            return False, -1
        
    print(count)
    return True, rotation_index


nums = [3,4,5,1,2]
#nums = [2,1,3,4]
is_valid, index = check(nums)
print(is_valid, index)