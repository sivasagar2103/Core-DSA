'''
Problem:
Given an array of meeting time intervals intervals[i] = [start, end],
determine if a person can attend all meetings.

key idea: Check overlap
Pattern: Sorting + Comparison

Intuition:
- Sort meetings by start time.
- Check if any meeting starts before the previous one ends.
- Overlapping intervals = impossible to attend all.
- Non-overlapping = possible.
- Sorting ensures we only need a single linear scan to detect overlap.

Time: O(nlog(n))
Space: O(1)

Sort by start --> check if next starts before previous ends.

'''

def can_attend_meetings(arr):
    arr.sort(key = lambda x: x[0])
    n = len(arr)

    for i in range(1, n):
        #current meeting start < previous meeting end -- overlap
        if arr[i][0] < arr[i-1][1]:
            return False
    return True

slots = [[0, 5], [6, 10], [11, 15]]
#slots = [[0,30],[5,10],[15,20]]
res = can_attend_meetings(slots)
print(res)
