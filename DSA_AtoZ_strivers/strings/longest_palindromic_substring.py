def longest_palindrome(word):

    if not word or len(word) == 1:
        return word
    
    n = len(word)
    start = 0
    max_len = 1

    def extend(left, right):
        while left >= 0 and right < n and word[left] == word[right]:
            left -= 1
            right += 1

        return left + 1, right - 1

    for i in range(n):
        l1, r1 = extend(i, i)
        diff1 = r1 - l1 + 1
        if diff1 > max_len:
            start = l1
            max_len = diff1
        
        l2, r2 = extend(i, i + 1)
        diff2 = r2 - l2 + 1
        if diff2 > max_len:
            start = l2
            max_len = diff2
        
    
    return word[start : start + max_len]

s = "babad"
res = longest_palindrome(s)
print(res)
