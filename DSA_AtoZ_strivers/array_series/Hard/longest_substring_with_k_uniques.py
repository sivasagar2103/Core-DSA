
def longest_k_substring(s, k):
    n = len(s)
    maxi = 0
    left = 0
    freq = {}
    start = 0

    for right in range(n):
        char = s[right]
        freq[char] = freq.get(char, 0) + 1

        while len(freq) > k:
            left_char = s[left]
            freq[left_char] -= 1
            if freq[left_char] == 0:
                del freq[left_char]
            left += 1
        
        if len(freq) == k:
            if right - left + 1 > maxi:
                start = left
                maxi = right - left + 1
    
    return maxi, s[start: start + maxi+1]


s = "aabacbebebe"
k = 3
res, sub = longest_k_substring(s, k)
print(res)
print(sub)