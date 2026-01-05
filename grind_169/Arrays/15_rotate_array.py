'''
Right Rotation:
rotate(0, n-1)
rotate(0, k-1)
rotate(k, n-1)


Left Rotation:
reverse(0, n-1)
reverse(0, n-k-1)
reverse(n-k, n-1)

Q. What if k is negative?
A. k = ((k%n) + n ) % n

Time: O(n)
Space: O(1)

Reverse all --> reverse first k --> reverse the rest.

'''


def rotate_array(arr, k):
    n = len(arr)
    k = k % n #if k > n

    def rotate(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    rotate(0, n-1)
    rotate(0, k-1)
    rotate(k, n-1)


nums = [1,2,3,4,5,6,7]
k = 3
rotate_array(nums, k)
print(nums)
#[5, 6, 7, 1, 2, 3, 4]