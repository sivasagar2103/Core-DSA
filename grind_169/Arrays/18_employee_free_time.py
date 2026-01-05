'''
Problem:
- Each employee's intervals represent when they are busy.
- We want to find when everyone is free at the same time.

I. First Approach
Core Idea:
All employees are free only during the gaps between merged busy intervals.
Flatten all schedules, sort by start time, merge overlaps,
and collect the gaps between merged intervals.

Steps of Implementation (Flatten + Sort + Merge)
1. Flatten all schedules
    Convert the list of employee schedules into a single list of intervals.
2. Sort intervals by start time
    Sorting ensures intervals are processed in chronological order.
3. Merge overlapping busy intervals
    Initialize a merged list with the first interval.
    For each interval:
    . If it overlaps with the last merged interval:
      . Extend the end time.
    . Else:
      . Append it as a new merged interval.
4. Find free time gaps
    Traverse merged intervals.
    The gap between:
    . merged[i-1].end and merged[i].start
    is a common free interval.
5. Return all free intervals

Time: O(n log n)   // sorting dominates
Space: O(n)        // flattened + merged intervals

2. Second Approach
Core Idea:
Use a min-heap to always process the earliest starting interval across employees.
Track the maximum end seen so far and detect gaps.

Steps:
1. Push the first interval of each employee into a min heap (by start time).
2. Pop the earliest interval:
    If its start > previous_end → free time found.
    Update previous_end.
3. Push the next interval from the same employee.
4. Continue until heap is empty.

Time: O(n log k)   // k = number of employees
Space: O(k)

Merge all busy times — the gaps are the free times.

'''

def find_employee_free_time(arr):
    intervals = [interval for emp in arr for interval in emp] #flatten
    intervals.sort(key = lambda x : x[0]) #sorted: #[[1,2], [1,3], [4,10],[5,6]]
    merged = [intervals[0]] #merged: [[1,3], [4,10]]

    n = len(intervals)
    for i in range(1, n):
        if intervals[i][0] <= merged[-1][-1]:
            merged[-1][-1] = max(merged[-1][-1], intervals[i][1])
        else:
            merged.append(intervals[i])
   
    #finding gaps
    free = []
    for i in range(1, len(merged)):
        free.append([merged[i-1][1], merged[i][0]]) #previous end and current start
    return free


def find_employee_free_time_two(arr):
    #using min heap
    pass

schedule = [
    [[1,2],[5,6]],
    [[1,3]],
    [[4,10]]
]
result = find_employee_free_time(schedule)
print(result)
