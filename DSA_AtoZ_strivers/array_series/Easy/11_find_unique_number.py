
'''
Why XOR Works:
Property of XOR ^	Description
a ^ a = 0	A number XORed with itself is 0
a ^ 0 = a	A number XORed with 0 is the number
Commutative & Associative	Order doesn't matter

'''

def find_unique(nums):
    result = 0
    for num in nums:
        result = result ^ num
    
    return result


nums = [4,1,2,1,2]
res = find_unique(nums)
print(res)
