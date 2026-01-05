'''
Core Idea:
Insert the new interval in the correct position and 
merge overlapping intervals in one pass.

Steps of implementation:
1. Initialize an empty result list (res) and an index i = 0.
2. Add all intervals that end before the new interval starts:
   - While intervals[i][1] < new_interval[0]:
     . Append intervals[i] to res
     . Move to the next interval
3. Merge all overlapping intervals with the new interval:
   - While intervals[i][0] <= new_interval[1]:
     . Update new_interval start = min(current start, new_interval start)
     . Update new_interval end = max(current end, new_interval end)
     . Move to the next interval
4. Append the merged new_interval to the result list.
5. Add all remaining intervals after the merged interval.
6. Return the result list.

Time: O(n)
Space: O(1)  (excluding the output list)

Add left non-overlaps, merge overlaps, then add right non-overlaps.

'''


def insert_interval(intervals, new_interval):
    res = []
    n = len(intervals)
    i = 0

    while i < n and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1
    
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1

    res.append(new_interval)

    while i < n:
        res.append(intervals[i])
        i += 1

    return res

intervals = [[1,3],[6,9]]
newInterval = [2,5]
res = insert_interval(intervals, newInterval)
print(res)
