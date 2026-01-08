'''
Problem:

Approach:

Time:
Space:

'''


def find_median(a,b):
    if len(b) < len(a):
        a, b = b, a
    n1, n2 = len(a), len(b)
    total = n1 + n2
    low = 0
    high = n1
    left = (total + 1)//2

    while low <= high:
        mid1 = (low + high)//2
        mid2 = left - mid1

        l1, l2 = float('-inf'), float('-inf')
        r1, r2 = float('inf'), float('inf')

        if mid1 >= 0:
            r1 = a[mid1]
        if mid2 >= 0:
            r2 = b[mid2]
        if mid1 - 1 < n1:
            l1 = a[mid1-1]
        if mid2-1 < n2:
            l2 = b[mid2-1]
        
        if l1 <= r2 and l2 <= r1:
            if total %2 == 1:
                return max(l1,l2)
            else:
                left = max(l1, l2)
                right = min(r1, r2)
                return (left + right)/2
        
        if l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return 0


arr1 = [2,4,6]
arr2 = [1,3,5]
res = find_median(arr1, arr2)
print(res)