
def frequency_sort(word):
    freq = {}

    for ch in word:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1
    
    n = len(word)
    buckets = ['' for _ in range(n+1)]

    for ch, count in freq.items():
        buckets[count] += ch * count
    
    return ''.join(buckets[i] for i in range(n-1,0,-1) if buckets[i])



s = "tree"
res = frequency_sort(s)
print(res)