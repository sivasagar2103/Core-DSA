'''
Each time we do: n & n-1
remove the lowest set bit
this runs in O(number of set bits) — which is O(log n) in the worst case.

'''

def count_set_bits(n):
    count = 0
    while n != 0:
        n = n & n-1
        count += 1
    return count

n = 5
res = count_set_bits(n)
print(res)