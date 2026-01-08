#separate list to save result
##Time : O(N), Space: O(N)

def insert(intervals, newInterval):
    res = []
    i = 0
    n = len(intervals)

    # Step 1: Add all intervals that end before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    # Step 2: Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)

    # Step 3: Add the remaining intervals
    while i < n:
        res.append(intervals[i])
        i += 1

    return res


# Test
print(insert([[1,3],[6,9]], [2,5]))  # [[1,5],[6,9]]



#inplace approach
#Time : O(N), Space: O(1)
def insert_inplace(intervals, newInterval):
    i = 0
    while i < len(intervals):
        # Case 1: current interval is completely before newInterval
        if intervals[i][1] < newInterval[0]:
            i += 1
            continue
        # Case 2: current interval is completely after newInterval
        elif intervals[i][0] > newInterval[1]:
            intervals.insert(i, newInterval)
            return intervals
        # Case 3: overlap -> merge
        else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            intervals.pop(i)
            continue
    intervals.append(newInterval)
    return intervals


# Test
print(insert_inplace([[1,3],[6,9]], [2,5]))  # [[1,5],[6,9]]
