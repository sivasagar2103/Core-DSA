'''
sliding window + hashmap

Core idea

Count each required character in t → need[ch].

Slide a window over s with two pointers left and right.

As you expand right, update have[ch].
When for some ch, have[ch] == need[ch], you have satisfied that character.

When all required characters are satisfied (formed == required), 
try to shrink from left to make the window as small as possible 
while staying valid. Track the best (shortest) window.

Intuition:
Use a sliding window with two pointers, track counts of required characters, 
expand right until all required characters are included, 
then shrink left to find the smallest valid window.

'''

def min_window(s, t):
    t_freq = {}
    
    for ch in t:
        if ch not in t_freq:
            t_freq[ch] = 0
        t_freq[ch] += 1
    
    required_count = len(t_freq)
    
    left = 0
    right = 0
    s_freq = {}
    current_count = 0
    n = len(s)
    min_length = n + 1
    start = 0
    
    while right < n:
        ch = s[right]
        if ch not in s_freq:
            s_freq[ch] = 0
        s_freq[ch] += 1
        
        if ch in t_freq and s_freq[ch] == t_freq[ch]:
            current_count += 1
        
        while left <= right and current_count == required_count:
            window_len = right - left + 1
            if window_len < min_length:
                min_length = window_len
                start = left
    
            left_ch = s[left]
            s_freq[left_ch] -= 1
            
            if left_ch in t_freq and s_freq[left_ch] < t_freq[left_ch]:
                current_count -= 1
            left += 1
            
        right += 1
        
    return s[start : start + min_length]
                

s = "ADOBECODEBANC"
t = "ABC"
res = min_window(s, t)
#Output: "BANC"
print(res)





