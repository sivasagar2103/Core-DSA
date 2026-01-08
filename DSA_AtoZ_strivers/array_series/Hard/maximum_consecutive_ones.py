
def maximum_consecutive_ones(nums, k):
    n = len(nums)
    z_count = 0
    maxi = 0
    left = 0

    for right in range(n):
        if nums[right] == 0:
            z_count += 1
        
        while z_count > k:
            if nums[left] == 0:
                z_count -= 1
            left += 1
        
        maxi = max(maxi, right - left +1)
    
    return maxi



nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
res = maximum_consecutive_ones(nums, k)
print(res)