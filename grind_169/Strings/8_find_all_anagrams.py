'''

Frequency Method + Sliding Window

'''

def find_anagrams(source, pattern):
    pattern_freq = {}
    pattern_len = len(pattern)

    for ch in pattern:
        if ch not in pattern_freq:
            pattern_freq[ch] = 0
        pattern_freq[ch] += 1
    
    source_freq = {}
    source_len = len(source)

    for i in range(pattern_len):
        char = source[i]
        if char not in source_freq:
            source_freq[char] = 0
        source_freq[char] += 1
    
    result = []
    
    if source_freq == pattern_freq:
        result.append(0)

    def matches():
        for ch in pattern_freq:
            if ch not in source_freq or source_freq[ch] != pattern_freq[ch]:
                return False
        return True

    for i in range(pattern_len, source_len):
        new_char = source[i]

        if new_char not in source_freq:
            source_freq[new_char] = 0
        source_freq[new_char] += 1

        old_char = source[i - pattern_len]
        source_freq[old_char] -= 1

        if matches():
            result.append(i - pattern_len + 1)
    
    return result


def find_anagrams_array_based(source, pattern):
    pass


s = "cbaebabacd"
p = "abc"
#Output: [0,6]
res = find_anagrams(s, p)
print(res)