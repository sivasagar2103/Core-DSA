'''
Ex: "12[a]"
'1' -> first digit
'2' -> second digit
If you just did: curr_num = int(ch)
Then,
curr_num = 1   (after seeing '1')
curr_num = 2   (after seeing '2') ❌ WRONG
You would lose the first digit and decode 2[a] instead of 12[a].

'''

def decodeString(s):
    num_stack = []
    str_stack = []
    
    curr_str = ""
    curr_num = 0
    
    for ch in s:
        if ch.isdigit():
            curr_num = curr_num * 10 + int(ch)
        
        elif ch == '[':
            num_stack.append(curr_num)
            str_stack.append(curr_str)
            curr_num = 0
            curr_str = ""
        
        elif ch == ']':
            repeat = num_stack.pop()
            prev = str_stack.pop()
            curr_str = prev + curr_str * repeat
        
        else:  # alphabet
            curr_str += ch
    
    return curr_str

def decodeStringSingleStack(s):
    stack = []
    curr_str = ""
    curr_num = 0

    for ch in s:
        if ch.isdigit():
            curr_num = curr_num * 10 + int(ch)
        
        elif ch == '[':
            stack.append((curr_str, curr_num))   # PUSH AS ONE TUPLE
            curr_str = ""
            curr_num = 0
        
        elif ch == ']':
            prev_str, repeat = stack.pop()
            curr_str = prev_str + curr_str * repeat
        
        else:   # alphabet
            curr_str += ch

    return curr_str


res = decodeString("3[a]2[bc]")  # "aaabcbc"
print(res)
