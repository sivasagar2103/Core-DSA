'''

expand around center

'''

def longest_palindromic_substring(sen):
    n = len(sen)

    def palindrome_edges(left, right):

        while left >= 0 and right < n and sen[left] == sen[right]:
            left -= 1
            right += 1
        
        return left+1, right-1

    maxi = 1
    start = 0
    for i in range(n):
        #odd length
        l1, r1 = palindrome_edges(i, i)

        #even length
        l2, r2 = palindrome_edges(i, i+1)

        diff1 = r1-l1+1
        diff2 = r2-l2+1

        if diff1 > maxi:
            maxi = diff1
            start = l1
        if diff2 > maxi:
            maxi = diff2
            start = l2
    
    return sen[start : start + maxi + 1]

s = "babad"
#Output: "bab"
res = longest_palindromic_substring(s)
print(res)
