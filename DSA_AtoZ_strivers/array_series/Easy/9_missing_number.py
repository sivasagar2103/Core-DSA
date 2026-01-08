
def find_number(arr):
    n = len(arr)
    sum_of_n = n * (n+1)//2
    arr_sum = sum(arr)
    return sum_of_n - arr_sum

def find_number_using_bits(arr):
    #using XOR operator
    n = len(arr)
    missing = n
    for i in range(n):
        missing = missing ^ i ^ arr[i]
    return missing


nums = [3,0,1]
res = find_number_using_bits(nums)
print(res)