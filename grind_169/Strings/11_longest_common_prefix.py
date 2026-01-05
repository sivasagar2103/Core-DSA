'''

'''

def common_prefix(words):
    min_word = words[0]
    min_length = len(min_word)

    result = []

    for word in words:
        if len(word) < min_length:
            min_word = word
            min_length = len(min_word)
    
    for i in range(min_length):
        current_char = words[0][i]

        for word in words[1:]:
            if word[i] != current_char:
                return ''.join(result)
        
        result.append(current_char)
    
    return ''.join(result)


strs = ["flower","flow","flour"]
res = common_prefix(strs)
print(res)
