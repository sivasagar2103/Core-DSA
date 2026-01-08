'''
Problem:
You are given an array of 'N' integers. You need to find the length of 
the longest sequence which contains the consecutive elements.

Approach:
1. Brute Force

Time: O(n**2)
Space = O(1)

2. Optimal
a. Sorting + Scanning
- Sort array in-place (O(n log n) time, O(1) space).
- Initialize counters to track the current consecutive sequence length 
and the longest length found.
- Iterate through the sorted array, for each element:
  a. If it's a duplicate of the previous, skip.
  b. If it extends the consecutive sequence (current == previous + 1), increment the count.
  c. Otherwise, reset the count.
- Track and update the maximum sequence length during traversal.
- Return the maximum length.

Time: O(n log n)
Space: O(1)

b. Using Set DS
- Put all elements in a hash set for O(1) access.
- For each number, check if it's the start of a sequence (i.e., 
the number just before it, num - 1, does not exist in the set).
- If it is the start, count how long the consecutive sequence is by 
increasing numbers one by one.
- Keep track of the maximum length found.

Time: O(n)
Space: O(n)

'''

def longest_seq_bf(arr):
    n = len(arr)
    count = 0

    def linear_search(next_num):
        for num in arr:
            if next_num == num:
                return True
        return False

    for i in range(n):
        ele = arr[i]
        temp = 1

        while linear_search(ele + 1):
            temp+=1
            ele += 1
        
        count = max(count, temp)
    
    return count

def longest_seq_op_ss(arr):
    n = len(arr)
    arr.sort()

    longest = 1
    current = 1

    for i in range(1, n):
        if arr[i] == arr[i-1]:
            continue
        elif arr[i] == arr[i-1] + 1:
            current += 1
        else:
            longest = max(longest, current)
            current = 1
    
    return max(longest, current)


def longest_seq_op_set(arr):
    arr_set = set(arr)
    longest = 0

    for num in arr:
        if num - 1 not in arr_set:
            current_num = num
            current_cnt = 1

            while current_num + 1 in arr_set:
                current_num += 1
                current_cnt += 1

        longest = max(current_cnt, longest)
    
    return longest


a = [100, 200, 1, 2, 3, 4]
res = longest_seq_op_set(a)
print(res)
#The longest consecutive sequence is 4.