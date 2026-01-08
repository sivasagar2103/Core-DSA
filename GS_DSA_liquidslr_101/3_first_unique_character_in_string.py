'''
Problem Statement

Given a string s, find the index of the first character
that appears exactly once in the string.
If no such character exists, return -1.

Approach Used:
1. one scan for frequency map and one scan for finding the element
2. Single scan with Queue data structure

Core Idea:
1. Frquency Map and search the character

Time:  O(n) + O(n) = 2O(n) ==> O(n)
Space: O(1)


2. A frequency map and a queue or ordered structure that keeps track of 
characters that are currently non-repeating.
- Remove if repeats
- front of the queue is always first non-repeating character.

Time: O(n) - single pass
Space: O(1)

'''
from collections import deque

def firstUniqChar(s: str) -> int:
    freq = {}
    n = len(s)
    for ch in s:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1
    
    for i in range(n):
        if freq[s[i]] == 1:
            return i
    return -1


def firstUniqChar_two(s: str) -> int:
    freq = {}
    q = deque()

    for i, ch in enumerate(s):
        if ch not in freq:
            freq[ch]  = 0
        freq[ch] += 1

        if freq[ch] == 1:
            q.append((ch, i))
        
        while q and freq[q[0][0]] > 1:
            q.popleft()#first from left
    
    return q[0][1] if q else -1


s = "leetcode"
res = firstUniqChar(s)
print(res)

result = firstUniqChar_two(s)
print(result)
