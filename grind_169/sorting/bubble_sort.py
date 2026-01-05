'''
Time : O(n**2)
Space: O(1)

1. start the loop from the last index[len(arr)-1] to 0. [i]
2. inner loop from 0 to i. [j]
3. swap the element if j > j+1
4. push the maximum element to the last index of the range.[0 to i]
5. After each iteration, the last element will be maximum element of array.
6. After n-1 iteration the array is sorted.
   If swap doesn't takes place, the array is already sorted and break the loop.

pros:
simplicity
Early exit if the list is sorted

cons:
not suitable for large data
too many swaps

'''

def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1,-1,-1):
        swap = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            print("break")
            break
                
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)
