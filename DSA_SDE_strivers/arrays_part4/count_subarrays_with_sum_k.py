'''
Problem:
Given an array of integers nums and an integer k, return the total number
of subarrays whose XOR equals to k.

Approach:
1. Brute-Force

Time: O(n**2)
Space: O(1)

2. Prefix XOR and HashMap


Time:
Space:

'''

def count_subarrays_bf(arr, target):
    n = len(arr)
    cnt = 0

    for i in range(n):
        curr = 0
        for j in range(i, n):
            curr = curr ^ arr[j]

            if curr == target:
                cnt += 1
    return cnt


def count_subarrays_ps(nums, target):
    n = len(nums)
    prefix_xor = 0
    xor_dict = {0:1}
    count = 0

    for i in range(n):
        prefix_xor ^= nums[i]
        desired = prefix_xor ^ target
        if desired in xor_dict:
            count += xor_dict[desired]

        xor_dict[prefix_xor] = xor_dict.get(prefix_xor, 0) + 1

    return count


nums = [4, 2, 2, 6, 4]
k = 6
res = count_subarrays_bf(nums, k)
print(res)
#The number of subarrays with XOR k is: 4
result = count_subarrays_ps(nums, k)
print(result)
