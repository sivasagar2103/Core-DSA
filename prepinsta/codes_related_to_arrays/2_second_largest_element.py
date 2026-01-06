
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


def second_largest_numbers(arr):
    n = len(arr)
    first, second = arr[0], arr[1]

    if second > first:
        first, second = second, first
    
    i = 0
    while i < n and arr[i] >= 0:
        i += 1
    
    if i == n:
        neg1, neg2  = 0, 0
    else:
        neg1, neg2 = arr[i], arr[i]

    for num in arr:
        if num > first:
            second = first
            first = num
        if num < first and num > second:
            second = num
        
        if num < 0:
            if num > neg1:
                neg2 = neg1
                neg1 = num
            if num < neg1 and num > neg2:
                neg2 = num
    
    return  [first, second, neg1, neg2]

arr = [8, 7, 6, 5, -3, -2, -5]
res = second_largest_numbers(arr)
print(res)

