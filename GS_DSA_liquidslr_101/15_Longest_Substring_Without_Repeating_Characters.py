'''
Problem Statement:
Given a string word, find the longest substring without repeating characters 
and return that substring.

Approach Used: Sliding Window + HashMap

Core Idea:
- Maintain a window [left, right] with no duplicate characters
- When a repeating character is found:
  . Move left to one position after the previous occurrence
- Track the maximum window size and its indices

Time: O(n)
Space: O(min(n, k))
Where k is the size of the character set (hashmap).

'''

def longest_substring(word):
    n = len(word)
    last_seen = {}
    left = 0
    max_length = 0
    start, end = 0, 0

    for right in range(n):
        char = word[right]

        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right

        diff = right- left + 1

        if diff > max_length:
            max_length = diff
            start = left
            end = right + 1
    
    return word[start : end]



s = "abcabcbb"
res = longest_substring(s)
print(res)
