'''
Intuition: [Weighted Interval Scheduling problem]
- Each job gives money, but only if it doesn't overlap with the previous one.
- So for every job, ask one question:
  . Should I include this job or skip it?
  . Which gives more profit?

core:
1. Given jobs with start, end, and profit.
2. Need to pick non-overlapping jobs to maximize profit.
3. This is a Weighted Interval Scheduling problem.

Steps:
1. Don't consider overlapping jobs.
2. Sort the jobs with end time to avoid overlapping. [ensures earlier finishing jobs come first.]
3. Binary search to get the last job that ends before it starts.
4. DP array (stores the best profit):
   include job [profit[i] + dp[last_non_conflict]] or 
   exclude job [dp[i-1]]
5. dp[n-1] gives the maximum profit.

Why Sorting by End Time Helps?
- We can make a DP where previous states always contain all jobs that end earlier.
- Binary search becomes possible on end times.

- Sort by end-time, DP+binary search

Time: O(nlogn)  [sorting (O(nlogn)) + binary search (O(logn)) + DP loop (O(n))]
Space: O(n) [dp array]

'''

def binary_search(jobs, i):
    #finding last non-overlapping job's index
    low = 0
    high = i-1
    ans = -1

    while low <= high:
        mid = (low + high) //2

        #current mid end <= previous start
        if jobs[mid][1] <= jobs[i][0]:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


def maximum_profit(start, end, profit):
    n = len(start)
    #sort by end
    jobs = sorted(zip(start, end, profit), key = lambda x: x[1])
    #0 - start, 1-end, 2-profit
    #1,3,50 ; 2,4,10 ; 3,5,40 ; 3,6,70

    #dp
    dp = [0] * n
    dp[0] = jobs[0][2]#profit will be saved in this array

    for i in range(1, n):
        incl = jobs[i][2]
        last = binary_search(jobs, i)
        if last != -1:
            incl += dp[last]

        excl = dp[i-1]

        dp[i] = max(incl, excl)

    print(dp)
    
    return dp[n-1]


start_time = [1,2,3,3]
end_time = [3,4,5,6]
profit = [50,10,40,70]
res = maximum_profit(start_time, end_time, profit)
print(res)
