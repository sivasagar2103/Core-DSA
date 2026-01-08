
# By using Boyer-Moore Majority Vote Algorithm
#This works only when the majority element is 
#guaranteed to exist, which is given in the problem.
def find_major_element(arr):
    count = 0
    cand = None

    for num in arr:
        if count == 0:
            cand = num
        count += 1 if cand == num else -1

    #if not gurantee
    if nums.count(cand) > len(arr)//2:
        return cand
    else:
        return - 1

nums = [2,2,1,1,1,1,2,2,2]
res = find_major_element(nums)
print(res)