from collections import Counter

def find_anagrams(s,p):
    res = []
    p_len = len(p)
    s_len = len(s)
    if p_len > s_len:
        return []
    
    p_count = Counter(p)
    window_count = Counter(s[:p_len])

    if p_count == window_count:
        res.append(0)
    
    for i in range(p_len, s_len):
        start_char = s[i - p_len]
        new_char = s[i]

        window_count[start_char] -= 1
        if window_count[start_char] == 0:
            del window_count[start_char]
        
        window_count[new_char] += 1

        if window_count == p_count:
            res.append(i-p_len+1)
    
    return res
    

s = "cbaebabacd"
p = "abc"
res = find_anagrams(s, p)
print(res)