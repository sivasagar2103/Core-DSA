
def longest_common_prefix(words):
    min_length = min(len(word) for word in words)
    res = []
    for i in range(min_length):
        char = words[0][i]
        for word in words:
            if word[i] != char:
                return ''.join(res)
        res.append(char)
    return ''.join(res)

strs = ["flower","flow","flight"]
res = longest_common_prefix(strs)
print(res)