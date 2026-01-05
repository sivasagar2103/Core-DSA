'''
1. Finding and incrementing the count by using array
- Since we are checking membership in array, inside loops,
  this version is O(n²) in worst case.

Time: O(n**2)
Space: O(1)

2. Convert the array into hashset for fast lookups (O(1))
- Each number processed once; set lookup O(1)
Time: O(n)
Space: O(n)

3. Sort the array and count the sequence
   . Sort the array in-place (O(n log n)).
   . Then linearly count consecutive elements.

Time: O(nlog(n))
Space: O(1)

Only numbers without a predecessor can start a new sequence.

'''

def longest_consecutive_sequence_first(arr):
    res = 0

    for num in arr:
        if num-1 not in arr:
            inc = 1
            while num+inc in arr:
                inc+=1
            res = max(inc, res)

    return res

def longest_consecutive_sequence_second(arr):
    arr_set = set(arr)
    res = 0
    for num in arr_set:
        if num-1 not in arr_set:
            inc = 1
            while num+inc in arr_set:
                inc+=1
            res = max(inc, res)

    return res


def longest_consecutive_sequence_third(arr):
    arr.sort()
    current = 1
    result = 1
    n = len(arr)

    for i in range(1, n):
        if arr[i] == arr[i-1] + 1:
            current += 1
        elif arr[i] == arr[i-1]:
            continue
        else:
            result = max(result, current)
            current = 1

    return max(result, current) #To handle last iteration, max is used.


nums = [100,4,200,1,3,2]
res = longest_consecutive_sequence_first(nums)
print(res)

res3 = longest_consecutive_sequence_third(nums)
print(res3)
