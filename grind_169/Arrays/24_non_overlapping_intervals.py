'''
Problem:
Non-overlapping Intervals

Core Idea:
To make intervals non-overlapping, remove the minimum number of intervals.
Whenever two intervals overlap, remove the one that ends later
(because it blocks more future intervals).

Intuition:
Sorting by start time lets us process intervals in chronological order.
When an overlap occurs:
    Keeping the interval with the smaller end time is optimal.
    It leaves more room for upcoming intervals.
Greedy choice at every overlap leads to a global optimum.

Steps of Implementation
1. Sort the intervals by start time.
2. Initialize:
    prev_end as the end of the first interval
    result = 0 (number of intervals removed)
3. Traverse intervals from the second one onward:
    If current.start < prev_end (overlap detected):
    . Increment removal count.
    . Update prev_end = min(prev_end, current.end)
    (drop the longer interval).
    Else:
    . No overlap → update prev_end = current.end.
4. Return the removal count.

Time: O(n log n)
Space: O(1)   (ignoring sort space)

On overlap, drop the interval that ends later.

'''


def find_non_overlapping(arr):
    n = len(arr)
    arr.sort(key = lambda x : x[0])
    #[[1,2],[1,3],[2,3],[3,4]]

    prev_end = arr[0][1]
    result = 0

    for i in range(1, n):
        start, end = arr[i]
        if start < prev_end:
            result += 1
            prev_end = min(prev_end, end)
        else:
            prev_end = end
    
    return result


intervals = [[1,2],[2,3],[3,4],[1,3]]
res = find_non_overlapping(intervals)
print(res)
