'''
Longest Substring Without Repeating Characters

Sliding Window + HashMap

Intuition:
- Use a sliding window and a hashmap to track the last seen index of each character.
- Expanding the window when characters are unique and shrinking 
it when duplicates occur.

Time: O(n)
Space: O(min(n, char_set))

'''

def longest_substring(sen):
    n = len(sen)
    last_seen = {}
    left = 0
    max_length = 0
    start, end = 0, 0

    for right in range(n):
        char = sen[right]

        #if character seen and inside current window → move left
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right

        diff = right - left + 1
        if diff > max_length:
            max_length = diff
            start = left
            end = right + 1

    
    print(sen[start : end])
    
    return max_length

s = "abcabcbb"
res = longest_substring(s)
print(res)
