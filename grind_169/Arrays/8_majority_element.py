'''
Boyer-Moore Voting Algorithm

Intuition:
Whenever the counter drops to zero, we choose a new candidate. 
Because the majority element appears more than half the time, 
it will survive all cancellations.

Time: O(n)
Space: O(1)

We can use HashMap count alternate approach.
Time: O(n)
Space: O(n)

| Problem            | Condition           | Valid Algorithm         |  
| ------------------ | --------------------| ----------------------- |
| Majority Element   | Appears > n/2 times | Boyer-Moore Voting works  |
| Contains Duplicate | Appears ≥ 2 times   | Hash Set or Sorting works |

'''

def major_element(arr):
    cand = None
    count = 0
    
    for element in arr:
        if count == 0:
            cand = element
        count += (1 if cand == element else -1)
    return cand

nums = [2,2,1,1,1,2,2]
res = major_element(nums)
print(res)
