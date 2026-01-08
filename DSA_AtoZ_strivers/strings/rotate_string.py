
def rotate_string(s, goal):
    if len(s) != len(goal):
        return False
    return goal in (s+s)

def rotate_string_kmp(s, goal):
    pass

s = "abcde"
goal = "cdeab"
res = rotate_string(s, goal)
print(res)