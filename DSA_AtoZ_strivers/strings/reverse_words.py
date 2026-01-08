'''
Why string concatenation (+) is more costly than list (array) joining:
1. Strings are immutable
- Every time we use s1+s2 operation, it creates a new string object in new memory location.
- i.e., The contents of s1 and s2 are copied into a new memory location.

2. Lists (arrays) are mutable
- We can append elements to array without copying the entire content.
- joining is done only once, at the end.

'''


def reverse_words(sen):
    n = len(sen)
    i = n - 1
    result = []

    while i >= 0:
        while i >= 0 and sen[i] == ' ':
            i -= 1
        if i < 0:
            break
        end = i
        while i >= 0 and sen[i] != ' ':
            i -= 1
        word = []
        for j in range(i+1, end+1):
            word.append(sen[j])

        result.append(''.join(word))
    
    return ' '.join(result)

def check_palindrome(sen):
    n = len(sen)
    left = 0
    right = n - 1

    while left < right:
        while left < right and not sen[left].isalnum():
            left += 1
        while left< right and not sen[right].isalnum():
            right -= 1
        if sen[left].lower() != sen[right].lower():
            return False
        left += 1
        right -= 1

    return True

s = "the sky is blue"
res = reverse_words(s)
print(res)
sen = "A man, a plan, a canal: Panama"
res = check_palindrome(sen)
print(res)