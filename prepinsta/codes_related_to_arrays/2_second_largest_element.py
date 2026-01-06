
def second_largest(arr):
    first = None
    second = None
    for val in arr:
        if first is None or val > first:
            second = first
            first = val
        
        elif val != first and (second is None or val > second):
            second = val
    
    return second


arr = [8, 8, 7, 6, 5]
res = second_largest(arr)
print(res)
