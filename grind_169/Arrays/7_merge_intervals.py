'''
Core Idea:
Intervals overlap if the start of the current interval is less than or equal to
the end of the previous merged interval.
Sort intervals by start time, then merge overlapping intervals in one pass.

1. Extra Space Approach
- Sort the intervals by their start value (if not already sorted).
- Initialize a result list with the first interval.
- Traverse remaining intervals:
  . If the current interval overlaps with the last merged interval:
    . Merge them by extending the end.
  . Otherwise:
    . Append the current interval to the result list.
- Return the result list.
- Time: O(n log n)  // sorting
- Space: O(n)       // result list

2. In-Place Approach
- Sort the intervals by start value.
- Maintain an index pointing to the last merged interval.
- Traverse the array:
  . If the current interval overlaps with the interval at index:
    . Merge by updating the end.
  . Otherwise:
    . Move index forward and overwrite the interval.
- Return the array up to index + 1.
- Time: O(n log n)
- Space: O(1)   // in-place (excluding sorting)

3. Already Sorted Intervals
- Apply either:
  . Extra space merging, or
  . In-place merging logic directly.
- Time: O(n)
- Space: O(1) or O(n) depending on approach

4. Merge Sort + Merge Intervals
- Use merge sort to divide the interval list into halves.
- While merging two sorted halves:
  . Apply interval overlap logic during the merge step.
- Ensure overlapping intervals are merged as they are combined.
- Final merged list is returned. 
- Time: O(n log n)
- Space: O(n)   // recursion + merged lists

Sort by start --> compare with last merged --> extend or append.

Note:
Overlap exists if:
current.start <= previous.end

'''

def merge_intervals_one(arr):
    #using extra space
    #if array is not sorted
    arr.sort(key = lambda x: x[0])
    n = len(arr)
    res = [arr[0]]

    for i in range(1, n):
        if arr[i][0] < res[-1][-1]:
            res[-1][-1] = max(res[-1][-1], arr[i][-1])
        else:
            res.append(arr[i])
    return res


def merge_intervals_two(arr):
    #inplace approach
    arr.sort(key = lambda x: x[0])
    n = len(arr)
    index = 0  #points to the last merged interval

    for i in range(1, n):
        if arr[i][0] < arr[index][1]:
            arr[index][1] = max(arr[i][1], arr[index][1])
        else:
            index += 1
            arr[index] = arr[i]

    return arr[:index+1]

def merge_intervals_three(arr):
    n = len(arr)
    #If the given input array is already sorted with first value at each index.
    #use any of the above approach without sorting

def merge_intervals_merge_sort(intervals):

    # merge two sorted lists of intervals AND merge overlaps
    def merge(left, right):
        merged = []
        i = j = 0

        # Standard merge sort merge, but with interval merging logic
        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                interval = left[i]
                i += 1
            else:
                interval = right[j]
                j += 1

            # merge logic here
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval[:])
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        # handle remaining items in left
        while i < len(left):
            interval = left[i]
            i += 1
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval[:])
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        # handle remaining items in right
        while j < len(right):
            interval = right[j]
            j += 1
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval[:])
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

    # merge sort but merging intervals as we go
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    return merge_sort(intervals)

   
intervals = [[1,3],[2,6],[8,10],[15,18]]
res = merge_intervals_one(intervals)
print(res)
res2 = merge_intervals_two(intervals)
print(res2)
