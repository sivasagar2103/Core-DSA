'''
Time : O(n**2)
Space : O(1)

outer-loop : i, inner-loop: j
i = 0 -- inner loop runs --> n-1 times
i = 1 -- inner loop runs --> n-2 times
.
.
(n-1) + (n-2) + . + . + ....
== (n*(n+1))//2

1. loop from o to n.
2. select an element as minimum [i].
3. inner loop from i + 1 to n [j].
4. compare the j and i elements. swap accordingly.
5. repeat the process.
6. At every step of outer loop ith element will be sorted.

'''

def selection_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
        i+=1

arr = [13,46,24,52,20,9]
selection_sort(arr)
print(arr)