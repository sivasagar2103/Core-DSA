'''

'''

def possible_combinations_I(arr, target):
    '''
    - A candidate may be selected from the pool an infinite number of times.

    Approach Steps:
    1. Sorting the input array:
       - It helps in early stopping.
       - avoids duplicates
    2. Recursive Backtracking function
       - start: tracks the current index
       - path: current partial combination
       - comb_sum: sum of elements in the current path
    3. Bounding Condition
       - Loop breaks when comb_sum + arr[i] > target

    Time: 
    O(N ** ( (T/M) + 1) )
    N - No. of element in array
    T - target sum
    M - minimum value in array
    ( The worst case occurs when you explore as many combinations as possible, 
      repeatedly picking the smallest element. )
    Avg case is much better than worst case, depends on the pruning of the search space.
    
    Space: 
    Auxilary Space: O(T/M) -  for the recursion stack and path
    Output Space: depends on the result

    '''
    arr.sort()
    result = []
    n = len(arr)

    def combinations(start, path, comb_sum):
        if comb_sum == target:
            result.append(path[:])
        

        for i in range(start, n):
            
            #bounding function to remove the search space
            if comb_sum + arr[i] > target:
                break

            path.append(arr[i])
            combinations(i, path, comb_sum+arr[i])
            path.pop()

    combinations(0, [], 0)
    return result


def possible_combinations_II(arr, target):
    '''

    
    '''
    result = []
    n = len(arr)
    arr.sort()

    def combinations(start, path, comb_sum):
        if comb_sum == target:
            result.append(path[:])
        
        for i in range(start, n):

            #clear the search space
            if comb_sum + arr[i] > target:
                break

            #avoid the duplicates
            if start > 0 and arr[i] == arr[i-1]:
                continue

            path.append(arr[i])
            combinations(i+1, path, comb_sum+arr[i])
            path.pop()

    combinations(0, [], 0)
    return result


def possible_combinations_III(arr, k, target):
    result = []
    n = len(arr)

    def combinations(start, path, comb_sum):
        if len(path) == k and comb_sum == target:
            result.append(path[:])

        if len(path) > k or comb_sum > target:
            return
        
        for i in range(start, n):

            #bounding function
            if arr[i] + comb_sum > target:
                break 

            path.append(arr[i])
            combinations(i+1, path, comb_sum+arr[i])
            path.pop()

    combinations(0, [], 0)

    return result


candidates = [2, 3, 5, 4]
target = 7
result = possible_combinations_I(candidates, target)
print(result)
# [ [2, 2, 3] , [3, 4] , [5, 2] ]
result_II = possible_combinations_II(candidates, target)
print(result_II)
# [[3, 4] , [5, 2] ]
nums = [i for i in range(1, 10)]
sub_set_size = 3
sub_set_target = 7
result_III = possible_combinations_III(nums, sub_set_size, sub_set_target)
print(result_III)