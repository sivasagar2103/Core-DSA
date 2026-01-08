'''

Approach:
HashMap Counting
Time: O(N)
Space: O(K)

'''

def check_anagram(s, t):
    if len(s) != len(t):
        return False

    char_count = {}
    for ch in s:
        if ch not in char_count:
            char_count[ch] = 0
        char_count[ch] += 1
    
    for ch in t:
        if ch not in char_count or char_count[ch] == 0:
            return False
        char_count[ch] -= 1
    
    return True


s = "anagram"
t = "nagaram"
res = check_anagram(s, t)
print(res)