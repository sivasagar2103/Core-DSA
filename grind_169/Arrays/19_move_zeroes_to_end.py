'''
Core Idea:
Shift all non-zero elements forward while preserving their relative order,
then fill the remaining positions with zeroes.

Steps of Implementation
1. Initialize an index pointer to track the position of the next non-zero element.
2. Traverse the array:
    If the current element is non-zero:
    . Place it at the index position.
    . Increment the index.
3. After processing all elements:
   . Fill the remaining positions from index to end with zeroes.
4. The array is modified in-place.

Time: O(n)
Space: O(1)

'''
def move_zeroes(arr):
    index = 0
    n = len(arr)

    for i in range(n):
        if arr[i] != 0:
            arr[index] = arr[i]
            index += 1
    
    for j in range(index, n):
        arr[j] = 0
    

nums = [0,1,0,3,12]
move_zeroes(nums)
print(nums)
