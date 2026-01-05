'''
Intuition:
- To find the k-th smallest among two sorted arrays,
  compare the k/2-th elements.
- If the k/2-th element of arr1 is smaller than the k/2-th element of arr2:
  then the first k/2 elements of arr1 are too small to be the k-th.

Core Idea:
- At each step, drop the smaller k/2 chunk from one array — repeat until k becomes 1.
- Keep two pointers i (arr1) and j (arr2).
- If one array runs out → the k-th element is in the other.
- If k = 1 → answer is the smaller of current elements.
- Otherwise
  . Look ahead k/2 positions in each array
  . Compare those elements.
  . ignore the k/2 smaller block.
  . reduce k
- prevents stepping beyond the array.
  . take = min(k//2, remaining_elements)

Time: O(logk)
Space: O(1)

'''

def find_kth_element(arr1, arr2, k):
    i = j = 0  # pointers

    while True:
        # If arr1 is exhausted → answer in arr2
        if i == len(arr1):
            return arr2[j + k - 1]

        # If arr2 is exhausted → answer in arr1
        if j == len(arr2):
            return arr1[i + k - 1]

        # If we need the smallest remaining element
        if k == 1:
            return min(arr1[i], arr2[j])

        # Check k//2 elements ahead in each array (stay in bounds)
        step1 = min(k // 2, len(arr1) - i)
        step2 = min(k // 2, len(arr2) - j)

        val1 = arr1[i + step1 - 1]
        val2 = arr2[j + step2 - 1]

        # Eliminate the smaller block
        if val1 < val2:
            i += step1      # drop step1 elements from arr1
            k -= step1
        else:
            j += step2      # drop step2 elements from arr2
            k -= step2


a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
res = find_kth_element(a, b, k)
print(res)
