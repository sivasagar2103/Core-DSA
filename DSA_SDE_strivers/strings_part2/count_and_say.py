'''
RLE Encoding

Time: O(2**N) : String length grows exponentially
Space: O(2**N) : Result string stored each iteration

'''

def count_and_say(n):

    def encode(string):
        n = len(string)
        res = []
        i = 0
        while i < n:
            count = 1
            while i + 1 < n and string[i] == string[i+1]:
                count += 1
                i += 1
            res.append(str(count) + string[i])
            i += 1
        return ''.join(res)


    current = "1"
    for i in range(1, n):
        current = encode(current)
    return current

def encode_string(word):
    n = len(word)
    prev = word[0]
    count = 1
    result = []

    for ch in word[1:]:
        if ch == prev:
            count += 1
        else:
            result.append(str(count) + ch)
            prev = ch
            count = 1
    result.append(str(count) + prev)
    return ''.join(result)


word = "AAABBB"
result = encode_string(word)
print(result)
n = 4
res = count_and_say(n)
print(res)
