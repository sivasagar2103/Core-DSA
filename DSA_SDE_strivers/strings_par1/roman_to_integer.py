'''
Time: O(n)                                              
Space: O(1)

'''

def roman_to_integer(roman):
    roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,
                 'D':500, 'M':1000}
    n = len(roman)
    end = n-1
    total = 0
    prev = 0

    while end >= 0:
        current = roman_map[roman[end]]
        if current < prev:
            total -= current
        else:
            total += current
            prev = current
        end -= 1
    
    return total
        

s = "DCCCXC"
res = roman_to_integer(s)
print(res)