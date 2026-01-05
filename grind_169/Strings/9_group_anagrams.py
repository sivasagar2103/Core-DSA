'''

'''


def group_anagrams(words):
    result = {}
    con = ord('a')

    for word in words:

        char = [0] * 26
        for ch in word:
            char_index = ord(ch) - con
            char[char_index] += 1
        
        char_freq = tuple(char)
        if char_freq not in result:
            result[char_freq] = []
        result[char_freq].append(word)
    
    return list(result.values())



strs = ["eat","tea","tan","ate","nat","bat"]
res = group_anagrams(strs)
print(res)