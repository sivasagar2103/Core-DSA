def reverse_an_array(arr):
    i = 0
    j = len(arr) - 1

    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

#By using recursion
def reverse_an_array_by_rec(arr):
    def rev_rec(i, j):
        if i >= j:
            return
        arr[i], arr[j] = arr[j], arr[i]
        rev_rec(i + 1, j - 1)

    rev_rec(0, len(arr) - 1)


arr = [1, 2, 3, 4]
reverse_an_array(arr)
print('reverse the source array',arr)
reverse_an_array_by_rec(arr)
print('reverse the reverse array to source',arr)