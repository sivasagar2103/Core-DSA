
def compress(chars):
    n = len(chars)
    write = 0
    i = 0

    while i < n:
        char = chars[i]
        count = 0

        while i < n and chars[i] == char:
            i += 1
            count += 1

        chars[write] = char
        write += 1

        if count > 1:
            for digit in str(count): #if len(number) > 1 - digits will split
                chars[write] = digit
                write += 1

    print(chars)
    print(chars[:write])

    return write

chars = ["a","a","a", "a", "b","b","c","c","c", "d"]
res = compress(chars)
print(res)
