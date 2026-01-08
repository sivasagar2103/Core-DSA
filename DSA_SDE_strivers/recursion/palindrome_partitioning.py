'''


Time:
- explores all possibilities - O(2 ** n)
- palindrome check - O(k) -- for every substring length (k)
- Total : O(n * 2 ** n)

Space:
- O(n) -- for recursive stack
- O(2**n) -- for exponential result

'''

def is_palindrome(start, end, word):
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True

def palindrome_partition(word):
    n = len(word)
    result = []

    def partition(start, path):
        if start == n:
            result.append(path[:])
            return
        
        for i in range(start, n):
            if is_palindrome(start, i, word):
                path.append(word[start : i+1])
                partition(i+1, path)
                path.pop()


    partition(0, [])
    return result


s = "aab"
res = palindrome_partition(s)
print(res)