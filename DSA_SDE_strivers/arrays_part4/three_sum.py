'''
Problem:
3 Sum : Find triplets that add up to a zero

Approach:
1. Brute Force

Time: O(n**2)
Space: O(n**2)

2. Sorting + Two Pointers
- Sort the array first -- O(nlogn)
- Fix one element at a time [i = 0]
- Two pointers for the remaining part [left = i+1, right = n-1]
- Adjust pointers based on sum:  -- 
    nums[left] + nums[right] = -nums[i] -- valid triplet -- move left+1 and right-1 
    if nums[left] + nums[right] < -nums[i] -- move left pointer -- left+1
    if nums[left] + nums[right] > -nums[i] -- move right pointer -- right-1
- skip duplicates over i, left and right

Time: 
For sorting : O(n log n) 
Two pointer: O(n**2)
Total : O(n**2)
Space: O(k)  --> k = no.of unique triplets

'''

def find_three_sum_bf(arr):
    n = len(arr)
    res = set()

    for i in range(n):
        temp_set = set()

        for j in range(i+1, n):
            third = -(arr[i] + arr[j])

            if third in temp_set:
                temp = [arr[i], arr[j], third]
                temp.sort()
                res.add(tuple(temp))

            temp_set.add(arr[j])
    
    return res


def find_three_sum_opt(arr):
    res = []
    n = len(arr)
    arr.sort() #O(nlogn) , [-1,-1,0,1,2,4]

    for i in range(n):

        if i != 0 and arr[i] == arr[i-1]:
            continue

        j = i+1
        k = n-1

        while j < k:
            total = arr[i] + arr[j] + arr[k]
            if total < 0:
                j+=1
            elif total > 0:
                k-=1
            else:
                res.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1

                while j < k and arr[j] == arr[j-1]:
                    j += 1
                while j < k and arr[k] == arr[k+1]:
                    k -= 1
        
    return res


nums = [-1, 0, 1, 2, -1, -4]
res = find_three_sum_bf(nums)
#Output: [-1 -1 2 ] [-1 0 1 ]
print(res)
result = find_three_sum_opt(nums)
print(result) 