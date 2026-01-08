def mobile_number_map(num_str):
    result = []

    keyboard_map = {
        "2": "abc", "3":"def", "4":"ghi",
        "5":"jkl","6":"mno", "7": "pqrs",
        "8": 'tuv',  "9" : "wxyz"
    }

    def backtrack(start, path):
        if start == len(num_str):
            result.append("".join(path[:]))
            return
        
        for letter in keyboard_map[num_str[start]]:
            path.append(letter)
            backtrack(start+1, path)
            path.pop()

    backtrack(0, [])
    return result

num = "237"
res = mobile_number_map(num)
print(res)
