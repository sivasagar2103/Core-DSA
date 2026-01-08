'''
Problem Statement:
- Given a list of characters chars, compress it in-place:
- Consecutive repeating characters are replaced by:
  . the character and followed by count (if count > 1)
- Return the new length after compression

Approach Used: Two Pointers (Read & Write)

Core Idea:
- Use one pointer (i) to read
- Use another pointer (write) to overwrite the compressed result in the same array
- Each iteration processes one group of identical characters.

Time: O(n)
Space: O(1)

'''

def compress_string(chars):
    write, i = 0, 0
    n = len(chars)

    while i < n:
        char = chars[i]
        start = i

        while i < n and chars[i] == char:
            i += 1
        
        chars[write] = char
        write += 1

        count = i - start
        if count > 1:
            #Handling multi-digit counts
            for dig in str(count):
                chars[write] = dig
                write += 1

    print(chars)
    print(chars[:write])

    return write

data = ["a","a","a","a","b","b","c","c","c","d"]
res = compress_string(data)
print(res) #7
