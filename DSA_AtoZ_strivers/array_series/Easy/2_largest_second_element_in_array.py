
def largest_second_element(arr):
    n = len(arr)
    if n < 2:
        return -1
    first = None
    second = None
    first_neg = sec_neg = None

    for num in arr:
        if num > 0:
            if first is None or num > first:
                second = first
                first = num
            elif num != first and (second is None or num > second):
                second = num

        if num < 0:
            if first_neg is None or num < first_neg:
                sec_neg = first_neg
                first_neg = num
            elif num != first_neg and (sec_neg is None or num < sec_neg):
                sec_neg = num

    return second if second is not None else -1, sec_neg if sec_neg else -1


nums = arr = [3, -1, 7, 2, -4, -9, 10, 5, -1]
pos, neg = largest_second_element(nums)
print(pos)
print(neg)