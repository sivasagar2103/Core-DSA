'''
KMP (Knuth-Morris-Pratt) Algorithm:
- Brute force search re-examines input text during mismatches.

Core Logic:
- Preprocessing Step
  . Build an LPS array (Longest Prefix Suffix) for the pattern.
  . The LPS position at i tells the longest proper prefix in the pattern that is also a suffix.
- Pattern Search Steo
  . Start comparing pattern with the text.
  . If characters mismatch, use the LPS table to skip unnecessary checks,
    move the pattern so previously matched prefix chars are reused
    without re-examining them.
  . Never move the search index in the text backwards.

Summary:
- KMP is a pattern matching algorithm that preprocesses the pattern into an LPS table,
  allowing efficient skips on mismatches, thus avoiding redundant comparisons.
- No backtracking in text; uses LPS to "remember" progress within the pattern.
- Efficient because it leverages repeated sub-patterns within the pattern itself 
  to minimize rechecking.

Time : O(N), N is the sixe of text
Space: O(M), M is size of pattern

Pros and Cons:

Rabin Karp (Rolling Hash):
Pros:
1. Multi-Pattern Search
2. Fast Average Performance (depends on hash function)
Cons:
1. Hash Collisons
2. False Positives
3. Not Always Linear
When to Use:
1. searching for multiple patterns at once ("dictionary matching").
2. patterns are relatively short and hash collisions are not a big concern.


KMP Algorithm (Longest Prefix Suffix)
Pros:
1. Guaranteed Linear Time (Always O(N))
2. No Collisions, No Hashing
Cons:
1. Best suited for searching one pattern at a time.
2. Extra Space (O(M) for lps array).
When to Use:
1. When you want guaranteed linear worst-case search speed.
2. When searching for a single pattern in text.
3. When the pattern contains internal repeats (KMP is especially effective).
4. When you want an algorithm that's robust against all data.

Note:
Use KMP if you need guaranteed linear time for a single pattern and you want 
to avoid any risk of hash collisions or false positives.
Use Rabin-Karp if you want to search for multiple patterns efficiently or value simplicity,
and the risk of hash collisions is low.

'''


#KMP
def find_pattern_kmp(text, pattern):
    m = len(pattern)
    lps_arr = [0] * m

    def build_lps(pattern):
        i = 0
        j = 1

        while j < m:
            if pattern[i] == pattern[j]:
                i += 1
                lps_arr[j] = i
                j += 1
            
            else:
                if i > 0:
                    i = lps[i-1]
                else:
                    lps_arr[j] = 0
                    j += 1


    lps = build_lps(pattern)
    a = 0
    b = 0
    n = len(text)

    while a < n:
        if text[a] == pattern[b]:
            a += 1
            b += 1

            if b == m:
                return a - b
        else:
            if b > 0:
                b = lps_arr[b-1]
            else:
                a += 1
    
    return -1

#Rabin-Karp
def find_pattern(text, pattern):
    d = 256
    prime = 7
    n = len(text)
    m = len(pattern)
    window_hash = 0
    pattern_hash = 0

    hash_value = 1
    for _ in range(m-1):
        hash_value = (d * hash_value) % prime
    
    #hash value for window and pattern
    for i in range(m):
        window_hash = ( d * window_hash + ord(text[i]) ) % prime
        pattern_hash = ( d * pattern_hash + ord(pattern[i]) ) % prime
    
    for j in range(n-m+1):
        if window_hash == pattern_hash:
            match = True
            for k in range(m):
                if text[j+k] != pattern[k]:
                    match = False
                    break
            if match:
                return j
        
        if j < n-m:
            window_hash = (d * (window_hash - ord(text[j]) * hash_value)
                           + ord(text[j+m]) )% prime
            if window_hash < 0:
                window_hash += prime
    return -1
        

haystack = "adbutsad"
needle = "sad"
res = find_pattern_kmp(haystack, needle)
print(res)