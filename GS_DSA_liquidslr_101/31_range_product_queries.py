'''
Note:
1. Fixed input + many queries?
   → Precompute

2. "Minimum powers of 2"?
   → Binary representation

3. Product of powers?
   → Sum of exponents

4. Range queries?
   → Prefix sums or small iteration

Problem:
- Given a positive integer n:
 . Construct an array powers consisting of the minimum number of powers of 2 
   whose sum is n
 . The array is sorted, unique, and deterministic
- Then for each query [l, r], compute:
  powers[l] * powers[l+1] * ... * powers[r]   (mod 1e9+7)

what is powers?
powers is simply the list of set bits of n, expressed as powers of 2.
n = 15 = 1111₂
powers = [1, 2, 4, 8]

Approach Used: Bit manipulation + prefix sums + fast exponentiation

Core Idea:
- Extract all set-bit exponents of n
- Build a prefix sum of exponents
- For each query:
  . Compute exponent sum in range
  . Answer = 2^(sum) mod 1e9+7

Time:
Extract bits: O(log n)
Prefix sum: O(log n)
Queries: O(q)
- Total: O(log n + q)
Space: powers / prefix arrays: O(log n)

'''

def product_queries(n, queries):
    MOD = 10 ** 9 + 7

    #1. exponents array
    exp = []
    bit = 0
    while n > 0:
        if n & 1:
            exp.append(bit)
        bit += 1
        n >>= 1
    
    print(exp)
    
    #2. prefix sum of exponents
    prefix = [0] * (len(exp) + 1)
    for i in range(len(exp)):
        prefix[i+1] = prefix[i] + exp[i] 
    
    print(prefix)

    #3. process queries
    res = []
    for l, r in queries:
        exp_sum = prefix[r+1] - prefix[l]
        res.append(pow(2, exp_sum, MOD))
    
    return res

n = 15
queries = [[0,1],[2,2],[0,3]]
res = product_queries(n, queries)
print(res)
#Output: [2,4,64]