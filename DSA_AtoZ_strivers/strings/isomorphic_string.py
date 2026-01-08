

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    s_map = {}
    t_map = {}

    for ch1, ch2 in zip(s, t):
        if ch1 in s_map:
            if s_map[ch1] != ch2:
                return False
        else:
            s_map[ch1] = ch2
        if ch2 in t_map:
            if t_map[ch2] !=ch1:
                return False
        else:
            t_map[ch2] = ch1
    
    return True



s = "egg"
t = "add"

res = is_isomorphic(s, t)
print(res)