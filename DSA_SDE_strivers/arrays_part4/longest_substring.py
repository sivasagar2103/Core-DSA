'''
Problem:
Length of Longest Substring without any Repeating Character

Approach:
1. Sliding Window + HashMap
- Empty dictionary char_index, left=0, maxi=0
- For each index right in word:
  . If word[right] seen and last_seen_index ≥ left, move left to (last_seen_index + 1)
  . Store/update word[right] last_seen_index = right
  . Update maxi = max(maxi, right - left + 1)
- return maxi

Time: O(n)
Space: O(min(m, n)) — depends on charset size

2. Knuth-Morris-Pratt (KMP)
- Array arr of size 128 with -1, start=0, max_len=0, max_start=0
- For each index end in word:
  . Convert word[end] to ASCII ascii_val
  . If arr[ascii_val] >= start, update start = arr[ascii_val] + 1
  . Update arr[ascii_val] = end
  . If current window length (end - start + 1) > max_len:
    . Update max_len and max_start
- Return: max_len, longest substring word[max_start:max_start + max_len]

Time: O(n)
Space: O(1) (fixed size array of 128)

Note: 
1. Dictionary approach is more flexible and works out-of-the-box for any input string,
including Unicode or extended character sets.
2. Array approach is more efficient in lookups (constant time) and uses less memory for 
fixed small alphabets like ASCII but requires knowledge of the character set in advance.

'''

def longest_substring_hm(word):
    last_seen_index = {}
    left = 0
    max_length = 0
    max_start = 0
    n = len(word)

    for right in range(n):

        if word[right] in last_seen_index and last_seen_index[word[right]] >= left:
            left = last_seen_index[word[right]] + 1

        last_seen_index[word[right]] = right
        if right - left + 1 > max_length:
            max_length = right - left + 1
            max_start = left
    
    return max_length, word[max_start : max_start + max_length]


def longest_substring_kmp(word):
    n = len(word)
    last_seen_index = [-1] * 128
    left = 0
    maxi = 0
    left_max = 0

    for right in range(n):
        ascii_value = ord(word[right])

        if last_seen_index[ascii_value] >= left:
            left = last_seen_index[ascii_value] + 1 

        last_seen_index[ascii_value] = right

        if right-left+1 > maxi:
            maxi = right-left+1
            left_max = left
    
    return maxi, word[left_max : left_max +maxi]



s = "abcabcbb"
maxi, word = longest_substring_hm(s)
print(maxi)
print(word)

maxi, word = longest_substring_kmp(s)
print(maxi)
print(word)