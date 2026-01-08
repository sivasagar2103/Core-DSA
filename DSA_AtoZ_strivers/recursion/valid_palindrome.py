def valid_palindrome(word):
    n = len(word)
    i = 0
    j = n - 1

    while i < j:
        if not word[i].isalpha():
            i += 1
            continue

        if not word[j].isalpha():
            j -= 1
            continue

        if word[i].lower() != word[j].lower():
            return False
        i += 1
        j -= 1

    return True

#by using recursion
def valid_palindrome_by_res(word):
    def helper_fun(word, i, j):
        if i >= j:
            return True
        
        while i < j and  not word[i].isalnum():
            i += 1
        
        while i < j and not word[j].isalnum():
            j -= 1

        if word[i].lower() != word[j].lower():
            return False
        
        return helper_fun(word, i + 1, j - 1)
    

    return helper_fun(word, 0, len(word) - 1)


name = "A man, a plan, a canal: Panama"
res = valid_palindrome(name)
result = valid_palindrome_by_res(name)
print(res)
print(result)
