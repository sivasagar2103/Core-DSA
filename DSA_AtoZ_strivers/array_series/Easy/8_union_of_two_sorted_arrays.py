'''
1. Two Pointer Approach
Time: O(n + m)
Space: O(1) extra space + O(n+m) [output list]

2. merge approach


'''

def find_union(arr1, arr2):
    i, j = 0, 0
    n1, n2 = len(arr1), len(arr2)
    result = []

    while i < n1 and j < n2:

        if arr1[i] < arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1

        elif arr2[j] < arr1[i]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1

        else:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i +=1
            j += 1
    
    while i < n1:
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1
    
    while j < n2:
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1
    
    return result


def find_intersection(arr1, arr2):
    i , j = 0, 0
    n1, n2 = len(arr1), len(arr2)
    res = []

    while i < n1 and j < n2:

        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1

        elif arr2[j] < arr1[i]:
            result.append(arr2[j])
            j += 1

        else:
            if not res or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
            j +=1

    return res


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]
result = find_union(nums1, nums2)
print(result)

res = find_intersection(nums1, nums2)
print(res)