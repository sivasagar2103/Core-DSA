
def min_bit_flipflops(start, goal):
    xor = start ^ goal
    count = 0
    while xor:
        xor = xor & xor -1
        count += 1
    return count


start = 10
goal = 7
res = min_bit_flipflops(start, goal)
print(res)