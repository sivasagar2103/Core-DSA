'''

Problem:
Given an integer array nums of size n. Return all elements which appear
more than n/3 times in the array. The output can be returned in any order.

Aproach:
Boyer-Moore Voting Algorithm

step-1:
- Initialize 4 variables: ele1, ele2, c1, c2
Step-2:
Traverse the array such that:
If cnt1 is 0 and current != ele2: ele1 = curent element and cnt1 = 1
If cnt2 is 0 and current != ele1: ele2 = curent element and cnt2 = 1
If current == ele1 --> cnt1 += 1
If current == ele2 --> cnt2 += 1
else: cnt1-=1, cnt2-=1
Step-3:
Manual Check once

Note:
>n/2 -- 1 element possible
>n/3 -- 2 elements possible
>n/k -- (k-1) elements possible


Time: O(n)
Space: O(1)

'''

def find_majority(nums):
    n = len(nums)
    ele1, ele2 = None, None
    c1, c2 = 0, 0

    for num in nums:
        if num == ele1:
            c1 += 1
        elif num == ele2:
            c2 += 1
        elif c1 == 0 and ele2 != num:
            ele1, c1 = num, 1
        elif c2 == 0 and ele1 != num:
            ele2, c2 = num, 1
        else:
            c1 -= 1
            c2 -= 1
    
    #check the count manually if the answer is correct or not
    tar = (n//3)
    count1, count2 = 0, 0
    for num in nums:
        if num == ele1:
            count1 += 1
        elif num == ele2:
            count2 += 1

    res = []
    if count1 >= tar:
        res.append(ele1)
    if count2 >= tar:
        res.append(ele2)
    
    print(res)

    return [ele1, ele2]


nums = [1, 2, 1, 1, 3, 2]
res = find_majority(nums)
print(res)