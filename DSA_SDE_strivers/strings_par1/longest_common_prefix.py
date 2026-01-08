'''
Horizontal scanning approach (also known as iterative prefix shrinking)

Time: O(n * m) -- n is the length of words, m is the length of shortest string
Space: O(1)

'''

def find_longest_common_prefix(words):
    prefix = words[0]

    for word in words[1:]:
        i = 0
        while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
            i += 1
        prefix = word[:i]
        if prefix == "":
            break
    
    return prefix


words = ["flowers" , "flow" , "fly", "flight" ]
res = find_longest_common_prefix(words)
print(res)