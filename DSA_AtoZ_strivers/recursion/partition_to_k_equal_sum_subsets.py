
def partition_results(arr, k):
    result = []
    arr.sort(reverse = True)
    total_sum = sum(arr)
    #If we can't evenly divide the total sum into k parts,
    # it's impossible to form equal subsets.
    if total_sum % k != 0:
        return False
    # This is the sum that each subset must add up to.
    target_sum = total_sum // k
    #If the largest number is bigger than the target subset sum,i
    #it's impossible to fit it into any subset — so return False.
    if arr[0] > target_sum:
        return False
    seen = [False] * len(arr)

    #start: the index to begin from in the nums array.
    # k: number of subsets still to form.
    #current_sum: running total of the current subset.
    def backtrack(start, k, current_sum):
        #Because if the first k-1 subsets are valid,
        # the last one must be valid with remaining elements.
        if k == 1:
            return True
        #if one subset is successfully formed (current_sum == target),
        # we start forming the next one by:
        #Resetting current_sum to 0, reducing k by 1
        if current_sum == target_sum:
            return backtrack(0, k-1, 0)
        
        for i in range(start, len(arr)):
            if current_sum + arr[i] <= target_sum and not seen[i]:
                seen[i] = True
                if backtrack(i+1, k, current_sum+arr[i]):
                    return True
                seen[i] = False
                #to skip empty subsets
                if current_sum == 0:
                    break
        
        return False
    return backtrack(0, k, 0)

def parition_results_list(arr, k):
    #TODO
    pass

    

nums = [4,3,2,3,5,2,1]
k = 4
result = partition_results(nums, k)
print(result)
