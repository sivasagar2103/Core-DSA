'''
Problem Statement:
Given a string sen, find the longest palindromic substring present in it.
A palindrome is a string that reads the same forward and backward.
If multiple answers exist, return any one of them.

Approach Used: Expand Around Center

Core Idea:
- Treat every index as a potential center of a palindrome.
- Expand left and right pointers while characters match.
- Track the longest palindrome found during the process.
- Return the substring using the stored start index and length.

Time: O(n²)
Each character can expand across the entire string in the worst case.
Space: O(1)

'''


def longest_palindromic_substring(sen):
    n = len(sen)

    start = 0
    maxi = 1

    def expand(left, right):
        #expand around centre
        while left >= 0 and right < n and sen[left] == sen[right]:
            left -= 1
            right +=1
        return left + 1, right - 1

    for i in range(n):
        l1, r1 = expand(i, i)
        l2, r2 = expand(i, i+1)

        diff1 = r1 - l1 + 1
        diff2 = r2 - l2 + 1

        if diff1 > maxi:
            maxi = diff1
            start = l1
        if diff2 > maxi:
            maxi = diff2
            start = l2
    
    return sen[start : start + maxi]


#Manacher algorithm is another approach: O(n), O(n)
s = "babad"
#Output: "bab"
res = longest_palindromic_substring(s)
print(res)
