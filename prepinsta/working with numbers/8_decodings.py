#Depth First Search Algorithm
'''
1. dfs(0, "")
num_string[0] = '1' → 'A'

→ dfs(1, "A")

num_string[0:2] = '12' → 'L'

→ will later call dfs(2, "L")

2. dfs(1, "A")
num_string[1] = '2' → 'B'

→ dfs(2, "AB")

num_string[1:3] = '23' → 'W'

→ dfs(3, "AW")

3. dfs(2, "AB")
num_string[2] = '3' → 'C'

→ dfs(3, "ABC")

4. dfs(3, "ABC") → i == len(num_string)
✅ Add "ABC" to result

🔙 Return to dfs(2, "AB") → done

5. dfs(3, "AW") → i == len(num_string)
✅ Add "AW" to result

🔙 Return to dfs(1, "A") → done

6. dfs(2, "L")
num_string[2] = '3' → 'C'

→ dfs(3, "LC")

7. dfs(3, "LC")
✅ Add "LC" to result

🔙 Return to dfs(2, "L") → done


'''

def get_decodings(num_str):
    result = []
    if len(num_str) == 0 or num_str[0] == '0':
        return result
    
    def dfs(i, path):
        if i == len(num_str):
            result.append(path)
            return

        if num_str[i] != '0':
            char = chr(64 + int(num_str[i]))
            dfs(i + 1, path + char)
        
        if i + 1 < len(num_str):
            dig = int(num_str[i : i+2])
            if 10 <= dig <= 26:
                dfs(i + 2, path + chr(64 + dig))
    
    dfs(0, "")
    return result

num_str = "123"
res = get_decodings(num_str)
print(res)
