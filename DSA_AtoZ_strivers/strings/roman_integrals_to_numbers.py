def convert_roman(sen):
    roman = {
        'I' : 1, 'V': 5, 'X':10,
        'L' : 50, 'C' : 100, 
        'D' : 500, 'M' : 1000
    }

    n = len(sen)
    i = n - 1
    total = 0
    prev = 0

    while i >= 0:
        current = roman[sen[i]]
        if current < prev:
            total -= current
        else:
            total += current
            prev = current
        i-=1
    
    return total


s = "MCMXCIV"
res = convert_roman(s)
print(res)