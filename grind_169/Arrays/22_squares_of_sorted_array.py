'''
Core Idea:
The input array is sorted, but squaring breaks the order because
negative numbers become positive.
The largest square will come from the number with the largest absolute value.
Use two pointers and fill the result array from the end.

Steps of Implementation (Two Pointers)
1. Initialize two pointers:
    left = 0
    right = n - 1
2. Create a result array of size n.
3. Use a position pointer starting from the end.
4. Compare absolute values at both ends:
    Place the larger square at res[pos].
5. Move the corresponding pointer inward.
6. Decrement pos.
7. Continue until pointers cross.

Time: O(n)
Space: O(n)

Q. Why we need to fill from last?
A. 1.The input array(arr) is sorted in ascending order. i.e., largest is at end
   2. When we sqaure, the negatives becomes positive and the largest is at end.
   3. If we start from the left(res[0]), we don't know the smallest square yet,
   because we are comparing absolute values from both ends.

'''


def sorted_squares(arr):
    #fill from the last or right
    n = len(arr)
    left = 0
    right = n-1
    res = [0] * n
    pos = n-1

    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            res[pos] = arr[left] ** 2
            left += 1
        else:
            res[pos] = arr[right] ** 2
            right -= 1
        pos -= 1
    return res


nums = [-4,-1,0,3,10]
res = sorted_squares(nums)
print(res)
