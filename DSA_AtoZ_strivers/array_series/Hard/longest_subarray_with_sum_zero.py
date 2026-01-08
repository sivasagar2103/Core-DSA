
def longest_subarray(arr):
    i = 0
    j = 1
    n = len(arr)
    maxi = 0

    while i < j:
        current = arr[i] + arr[j]
        if current == 0:
            maxi = max(j+ 1, maxi)


arr = [15, -2, 2, -8, 1, 7, 10, 23]
res = longest_subarray(arr)
print(res)