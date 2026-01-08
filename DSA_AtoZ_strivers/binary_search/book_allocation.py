'''
1. Define binary search space between max of books and total pages.
2. Use mid as a candidate answer, then simulate allocation.
3. Count how many students are needed for current mid (max pages limit).
4. If more students required → move right.
5. If students ≤ m → store answer and try smaller (move left).
6. Return the lowest max pages where allocation is valid.

Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), 
where N = size of the array, sum(arr[]) = sum of all array elements, 
max(arr[]) = maximum of all array elements.
Reason: We are applying binary search on [max(arr[]), sum(arr[])].
Inside the loop, we are calling the countStudents() function for the value 
of mid. Now, inside the countStudents() function, 
we are using a loop that runs for N times.
Space Complexity:  O(1)

'''


def find_pages(books, students):

    def count_students(arr, limit):
        partitions = 1
        pages = 0
        for num in arr:
            if pages + num <= limit:
                pages += num
            else:
                partitions += 1
                pages = num
        return partitions

    low = max(books)
    high = sum(books)

    while low <= high:
        mid = (low + high) //2
        partitions = count_students(books, mid)
        print(partitions)
        if partitions > students:
            low = mid + 1
        else:
            high = mid - 1
    return low


nums = [12, 34, 67, 90]
m=2
result = find_pages(nums, m)
print(result)