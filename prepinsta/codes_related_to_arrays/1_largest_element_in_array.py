
def largest_element(arr):
    large_positive = arr[0]
    largest_negative = None
    for i in range(1, len(arr)):
        if arr[i] == large_positive:
            continue
        if arr[i] > large_positive:
            large_positive = arr[i]
        if arr[i] < 0:
            if largest_negative is None or arr[i] > largest_negative:
                largest_negative = arr[i]
    return large_positive, largest_negative


arr = [3, 3, 6, 1, -3, -2, -1]
pos, neg = largest_element(arr)
print(pos, neg)
