'''
Problem Statement:
Given an array of intervals where intervals[i] = [start, end],
merge all overlapping intervals and return the resulting list
of non-overlapping intervals that cover all the intervals in the input.

Approach Used:
- Sorting + Greedy

Core Idea:
- After sorting, overlapping intervals appear next to each other.
- Maintain an index pointing to the last merged interval.
- If the current interval overlaps with the last merged one,
  extend the end of the last interval.
- Otherwise, move forward and treat the current interval as a new interval.

Time:
- O(n log n) due to sorting.

Space:
- O(1) extra space (in-place merging, excluding output).

'''

def merge_intervals(arr):
    arr.sort(key = lambda x: x[0]) #if not sorted
    n = len(arr)
    idx = 0

    for i in range(1, n):
        if arr[i][0] <= arr[idx][1]:
            arr[idx][1] = max(arr[i][1], arr[idx][1])
        else:
            idx += 1
            arr[idx] = arr[i]
    
    return arr[:idx+1]



intervals = [[1,3],[2,6],[8,10],[15,18]]
res = merge_intervals(intervals)
print(res)
