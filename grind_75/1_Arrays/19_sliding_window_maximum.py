
def maximum_of_sliding_window_bf(arr, k):
    '''
    Time: O(n * k)
    Sapce : result + O(n)
    
    '''
    result = []
    n = len(arr)

    for i in range(n - k + 1):
        temp = arr[i : i+k]
        result.append(max(temp))

    return result


def maximum_of_sliding_window_heap(arr, k):
    pass


nums = [1,3,-1,-3,5,3,6,7]
k = 3
#Output: [3,3,5,5,6,7]
result = maximum_of_sliding_window_bf(nums, k)
print(result)

res = maximum_of_sliding_window_heap(nums, k)
print(res)

