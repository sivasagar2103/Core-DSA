'''

'''

def valid_palindrome(sen):
    n = len(sen)
    i = 0
    j = n-1

    while i < j:
        
        while i < j and not sen[i].isalnum():
            i += 1
        while i< j and not sen[j].isalnum():
            j -= 1
        
        if sen[i].lower() != sen[j].lower():
            return False
        
        i += 1
        j -= 1
    
    return True


s = "A man, a plan, a canal: Panama"
res = valid_palindrome(s)
print(res)
