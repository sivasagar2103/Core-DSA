
def aggressive_cows(nums, k):

    def calculate_distance(mid):
        cows_count = 1
        for num in nums:
            if 






    nums.sort()
    n = len(nums)
    low = 1
    high = nums[n-1] - nums[0]

    while low <= high:
        mid = (low + high) //2
        dist = calculate_distance(mid)




n = 6
k = 4
nums = [0, 3, 4, 7, 10, 9]
