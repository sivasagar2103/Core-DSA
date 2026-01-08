def unique_characters(arr):
    def unique(a):
        return len(set(a)) == len(a)

    arr = [a for a in arr if unique(a)]

    def backtrack(start, current):
        if len(set(current)) < len(current):
            return 0
        
        max_len = len(current)
        for i in range(start, len(arr)):
            max_len = max(max_len, backtrack(i+1, current+arr[i]))
        return max_len


    return backtrack(0, "")


def unique_characters_combinations(arr):
    #TODO
    pass

str_arr = ["un","iq","ue"]
result = unique_characters(str_arr)
print(result)