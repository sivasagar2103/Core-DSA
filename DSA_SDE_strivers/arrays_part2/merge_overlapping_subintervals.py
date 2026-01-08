'''
Problem:

Approach:
*Brute Force
1. sort the intervals(sorting will takes place based on the first element of interval, if the first
two elements are equal, it consider the second element).
2. If the next interval starts before or when the current one ends, merge them by updating 
the end to the maximum of both ends.

Time: O(NlogN)+O(2N)
Space: O(N)

*Optimal:
- Traverse each interval from the second onward:
  1. If the current interval overlaps with the last one in the result 
  (i.e., current start ≤ last end),merge them by updating the last interval's 
  end to the maximum end.
  2. If it doesn't overlap, simply add the current interval to the result list.

Time: O(NlogN)+O(N)
Space: O(N)

'''
#brute force
def merge_subintervals_bf(matrix):
    matrix.sort() #O(nlogn)
    n = len(matrix)
    res = []

    for i in range(n): #O(2n)
        start = matrix[i][0]
        end = matrix[i][1]

        #Skip the intervals that are already merged in the result.
        if res and end <= res[-1][-1]:
            continue
        
        #update the second element with maximum one
        for j in range(i+1, n):
            if end > matrix[j][0]:
                end = max(end, matrix[j][1])

            else:
                break
        res.append([start, end])

    return res

def merge_subintervals_optimal(matrix):
    n = len(matrix)
    matrix.sort()
    res = []

    for i in range(n):
        #if the current interval does not
        # lie in the last interval of the res:
        if not res or matrix[i][0] > res[-1][-1]:
            res.append(matrix[i])
        # if the current interval
        # lies in the last interval:
        else:
            res[-1][-1] = max(res[-1][1], matrix[i][1])
    
    return res

intervals = [[1,5],[3,6],[8,10],[15,18]]
res = merge_subintervals_optimal(intervals)
print(res)
