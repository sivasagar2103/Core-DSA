

def reverse_words(sen):
    n = len(sen)
    i = n-1
    res = []

    while i >= 0:
        while i >= 0 and sen[i] == ' ':
            i-=1
        if i < 0:
            break
        end = i
        while i >= 0 and sen[i] != ' ':
            i-=1
        chars = []
        for j in range(i+1, end+1):
            chars.append(sen[j])
        res.append(''.join(chars))
    
    return ' '.join(res)
        

s = "  hello world  "
res = reverse_words(s)
print(res)