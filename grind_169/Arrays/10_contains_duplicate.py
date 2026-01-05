'''
Core Idea:
While traversing the array, check whether an element has already been seen.
If yes, a duplicate exists; otherwise, remember the element.

Steps of implementation:
1. Create an empty set to store elements that have already been seen.
2. Traverse the array one element at a time:
   - If the current element is already in the set:
     . Return True (duplicate found).
   - Otherwise:
     . Add the element to the set.
3. If the traversal completes without finding duplicates:
   - Return False.

Time: O(n)
Space: O(n)

Set lookup is O(1) on average

'''

def contains_duplicate(arr):
    arr_set = set()
    for element in arr:
        if element in arr_set:
            return True
        arr_set.add(element)
    return False

nums = [1,2,3,1]
res = contains_duplicate(nums)
print(res)
