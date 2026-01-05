'''

'''

def valid_anagram(s, t):

    if len(s) != len(t):
        return False

    s_to_t = {}

    for ch in s:
        if ch not in s_to_t:
            s_to_t[ch] = 0
        s_to_t[ch] += 1
    
    for ch in t:
        if ch not in s_to_t:
            return False
        s_to_t[ch] -= 1
        if s_to_t[ch] < 0:
            return False
    
    return True

s = "anagram"
t = "nagaram"
res = valid_anagram(s, t)
print(res)