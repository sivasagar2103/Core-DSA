'''
Problem:
There is one meeting room in a firm. You are given two arrays, 
start and end each of size N.
For an index i, start[i] denotes the starting time of the ith meeting 
while end[i]  will denote the ending time of the ith meeting. 
Find the maximum number of meetings that can be accommodated if only
one meeting can happen in the room at a  particular time. 
Print the order in which these meetings will be performed.

Approach: 
Core Idea: Choosing meetings that end earliest ensures the meeting room 
           frees up sooner, allowing more subsequent meetings to be scheduled.
            Choosing longer or later-ending meetings could block the room unnecessarily,
            limiting the total count.
- Combine and index meetings: list of (start, end, index starts from 1)
- Sort by ending times:
  Sort the meetings based on their end times in ascending order
  [Note: Greedy Choice, Optimal Substructure
  Sorting by end time implements the earliest finish time first greedy strategy,
  which is proven to give the optimal answer to the "maximum meetings in one room" problem.
  ]
- Greedy selection:
  . Initialize a variable limit as the end time of the first meeting in the sorted list.
  . Select the first meeting and add its number to the results list.
  . Iterate over the sorted meetings from the second one onward:
    . If a meeting's start time is strictly greater than the limit,
      select it, add it to the answer, and update limit with this meeting's end time.
    . If it overlaps (start time ≤ limit), skip it.

Time: O(N log N) for sorting + O(N) for selecting meetings → O(N log N) overall.
Space: O(N) extra space to store combined meeting info and output order.

'''
def maximum_meetings(start, end, n):
    meetings = [(start[i], end[i], i+1) for i in range(n)]
    meetings.sort(key = lambda x: x[1]) #sort by end time

    #0 - start, 1 - end, 2 - position 
    limit = meetings[0][1]
    res = [1]

    for i in range(1, n):
        #start > end
        if meetings[i][0] > limit:
            limit = meetings[i][1]
            res.append(meetings[i][2])
    
    return res

n = 6
start = [1,3,0,5,8,5]
end = [2,4,5,7,9,9]
res = maximum_meetings(start, end, n)
print(res)
#Output: [1 2 4 5]
