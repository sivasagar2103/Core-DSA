'''
Time : O(n**2)
Space : O(1)

1. run a loop from 1st index[1] to the end. [i]
2. Compare it with elements before it (to the left).
3. Shift all larger elements one position to the right.[
    run an inner loop from i-1 to 0. [j]]
4. Insert the current element at its correct position in the sorted part.
5. Repeat steps 2-4 for all remaining elements.


'''

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        temp = arr[i]
        j = i-1
        
        while j >=0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = temp

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array:", arr)