
def rotate_array(nums, k):
    n = len(nums)
    k = k % n #if k > n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]

            start += 1
            end -= 1
    
    reverse(0, n-1)
    #[7,6,5,4,3,2,1]
    reverse(0, k-1)
    reverse(k, n-1)


nums = [1,2,3,4,5,6,7]
#o/p: [5,6,7,1,2,3,4]
k = 3
rotate_array(nums, k)
print(nums)