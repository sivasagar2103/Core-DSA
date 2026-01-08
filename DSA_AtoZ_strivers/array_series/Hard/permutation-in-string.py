from collections import Counter

def find_permutation(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)

    s1_count = Counter(s1)
    window = Counter(s2[:s1_len])

    for i in range(s1_len, s2_len):
        start = s2[i - s1_len]
        new_char = s2[i]

        window[start] -= 1

        if window[start] == 0:
            del window[start]
        
        window[new_char] += 1

        if s1_count == window:
            return True
    
    return False


s1 = "abc"
s2 = "eidbacooo"
res = find_permutation(s1, s2)
print(res)