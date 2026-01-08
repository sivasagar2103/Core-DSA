'''

Sorting ensures that events happen in time.

'''

def minimum_meeting_rooms_two_pointers(arr):
    start_times = sorted(i[0] for i in arr)
    end_times = sorted(i[1] for i in arr)

    start = 0
    end = 0
    current = 0
    maxi = 0

    n = len(arr)

    while start < n:
        if start_times[start] < end_times[end]:
            current += 1
            start += 1
        else:
            current -= 1
            end += 1
        maxi = max(maxi, current)

    return maxi

def minimum_meeting_rooms_heap(arr):
    pass


meetings = [[0,30],[5,10],[15,20]]
res = minimum_meeting_rooms_two_pointers(meetings)
print(res)

result = minimum_meeting_rooms_heap(meetings)
print(result)

