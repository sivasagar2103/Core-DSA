'''

'''

def print_all_subsequences(arr):
    n = len(nums)
    result = []

    def subsequences(start, path):
        result.append(path[:])
        
        for i in range(start, n):
            path.append(arr[i])
            subsequences(i+1, path)
            path.pop()

    subsequences(0, [])
    return result


def longest_increasing_subsequence(arr):
    pass



nums = [10, 9, 2]
#Output: 4
res = print_all_subsequences(nums)
print(res)