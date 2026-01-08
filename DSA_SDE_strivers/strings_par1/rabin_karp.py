'''

Steps of Rabin Karp Algorithm: [Also called as Rolling Hash Function]
- Calculate Hash Function for pattern
- Calculate Hash Function for window in text
- Repeat the following until text ends
  . If hash(pattern) == hash(window text) -- match chars one by one
  . subtract left most(MSB) from text window hash value.
  . Add new character to the window.

How to build sronger hash function?
alphabet size, d= 26
prime number, p = 5381 (longest prime number)
window size, m = 3
len(text) = n

Approach Steps:
- Preprocessing
 . choose a base, d = 256 and larger prime number to minimise collisions, prime = 5381
 . precompute a high order multiplier that will be used in rolling hash updates
   h = (d ** (m-1)) % prime, m --> length of pattern
- Hash Computation
  . Compute the hash of the pattern and first window of the text(substring of length m).
- Sliding Window and Matching
  . slide the window through the text from o to n-m.
    .If the window hash equals the pattern hash, verify by checking characters one by one.
    . Update the window hash using the rolling hash formula:
       next_hash = ( d * (curent_hash - old_char * h) + new_char )% prime
    . repeat for all the windows.


Time: O(n+m)
O(n*m) : if every hash collides and you verify each window, which is rare with a good hash
Space: O(1)



'''

def sublist_search(text, pattern):
    result = []
    n = len(text)
    m = len(pattern)

    prime = 5381
    d = 256
    window_hash = 0
    pattern_hash = 0

    hash_value = 1
    for _ in range(m-1):
        hash_value = (hash_value * d) % prime
    
    #finding text hash for frst window and pattern hash
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % prime
        window_hash = (d * window_hash + ord(text[i])) % prime
    

    for j in range(n-m+1):
        if pattern_hash == window_hash:
            match = True
            for k in range(m):
                if text[j+k] != pattern[k]:
                    match = False
                    break
            if match:
                result.append(j)
        
        if j < n-m:
            window_hash = (
                            d * (window_hash - ord(text[j]) * hash_value) 
                            + ord(text[j+m])
                          ) % prime

            if window_hash < 0:
                window_hash += prime
    
    return result

text = "ababcabcababc"
pattern = "abc"
result = sublist_search(text, pattern)

#Output: [2, 5, 10]
print(result)