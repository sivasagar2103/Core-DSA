'''
Problem Statement
Given an array of strings, group the anagrams together.
Anagrams are words that have the same character counts, possibly in different orders.

Approach Used: 
Character Frequency Hashing

Core Idea:
- Two strings are anagrams if and only if their character frequency counts are identical
- Convert frequency list into a tuple (hashable)
- Use the tuple as the dictionary key

n = number of words ; k = average word length
Time: O(n * k)
Space: O(n * k)

'''

def group_anagrams(words):
    result = {}
    base = ord('a')

    for word in words:
        freq = [0] * 26

        for ch in word:
            idx = ord(ch) - base
            freq[idx] += 1

        key = tuple(freq)
        result.setdefault(key, []).append(word)

    return list(result.values())
    

strs = ["eat","tea","tan","ate","nat","bat"]
res = group_anagrams(strs)
print(res)
