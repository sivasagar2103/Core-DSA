'''
Intuition:
- Count the frequency of each character, add all even counts, and for odd counts,
  take the largest even part plus one central character if available.
Time: O(n)
Space: O(k)

a - 1
b - 1
c = 4
d - 2

'''

def longest_palindrome(sen):
    freq = {}
    for ch in sen:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1
    
    res = 0
    odd = False

    for val in freq.values():
        if val % 2 == 0:
            res += val
        else:
            # take the even part
            res += val - 1
            odd = True
    
    if odd:
        res += 1
    
    return res

s = "abccccdd"
res = longest_palindrome(s)
print(res)
