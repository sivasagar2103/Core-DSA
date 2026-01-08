'''
Problem:
The majority element of an array is an element that appears more than n/2 times
in the array. The array is guaranteed to have a majority element.

Approach:
1. Bruteforce

2. Optimal : Moore's Voting
step-1:
Initialize 2 variables:
Count - for tracking the count of element
Element - for which element we are counting
step-1:
Traverse through the given array.
If Count is 0 then store the current element of the array as Element.
If the current element and Element are the same increase the Count by 1.
If they are different decrease the Count by 1.
The integer present in Element should be the result we are expecting 

Note: If the question states that the array must contain a majority element, 
in that case, we do not need the second check. 
Then the time complexity will boil down to O(N).

Time: O(n) + O(n) ==> 2O(n)
Space: O(1)

'''

def major_element_bf(nums):
    n = len(nums)

    for i in range(n):
        cnt = 0
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                cnt += 1
        
        if cnt >= (n//2):
            return nums[i]
    return -1


def majority_element(nums):
    #voting algorithm
    count = 0
    element = None
    n = len(nums)

    for i in range(n):
        if count == 0:
            count = 1
            element = nums[i]
        elif nums[i] == element:
            count += 1
        else:
            count -= 1
    
    #if must contain the above element value contains the result
    #O(n)

    #In case may be or not, we need to cross verify
    cnt = 0
    for j in range(n):
        if nums[j] == element:
            cnt += 1
    if cnt >= (n//2):
        return element
    else:
        return - 1
    #O(n)
    

nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
res = major_element_bf(nums)
print(res)
result = majority_element(nums)
print(result)
