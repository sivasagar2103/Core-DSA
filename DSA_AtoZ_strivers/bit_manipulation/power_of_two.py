
'''
A power of two in binary has exactly one bit set (
e.g., 1=0b1, 2=0b10, 4=0b100, 8=0b1000)
Subtracting 1 from it flips the lowest set bit and sets all lower bits to 1
Bitwise AND with the original clears all bits → becomes zero
Ex: 8 - 1000
    7 - 0111
8 & 7 - 0000    

'''

def is_power_of_two(n):
    return n > 0 and (n & n-1) == 0


num = 8
res = is_power_of_two(num)
print(res)