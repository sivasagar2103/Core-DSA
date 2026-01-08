'''
Problem:
We are given two arrays that represent the arrival and departure times of trains
that stop at the platform. We need to find the minimum number of platforms 
needed at the railway station so that no train has to wait.

Approach:
- Sort times: Align arrival/departure events for easier comparison
- Use two pointers: Walk through both arrays to simulate platform usage
- Increment/Decrement: Track platforms needed in real-time at each event
  . Start both pointers at the beginning (i=1, j=0).
  . If the next train arrives before or at the same time as the 
    current earliest departure (arr[i] <= dep[j]): 
      . Increment count, move the arrival pointer forward.
  . Otherwise (arr[i] > dep[j]):
      . Decrement count, move the departure pointer forward.
- return result


Time: O(NlogN)
Space: O(1)

'''

def minimum_platforms_bf(start, end, n):
    start.sort()
    end.sort()

    res= 1
    count = 1

    i = 1
    j = 0

    while i < len(start) and j < len(end):
        if start[i] <= end[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1
        res = max(res, count)
    
    return res




n = 6
start_time = [900, 945, 955, 1100, 1500, 1800]
end_time = [920, 1200, 1130, 1150, 1900, 2000]
res = minimum_platforms_bf(start_time, end_time, n)
print(res)


