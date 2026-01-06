'''
if num >= 100:
    word += ones[num // 100] + " hundred "
    num %= 100
    if num:
        word += " and "
if num >= 20:
    word += tens[num // 10]
    if num % 10:
        word += "-" + ones[num % 10]

Both if conditions are independent.
That means both can run, one after the other, if their conditions are true.

if num >= 100:
    word += ones[num // 100] + " hundred "
    num %= 100
    if num:
        word += " and "
elif num >= 20:
    word += tens[num // 10]
    if num % 10:
        word += "-" + ones[num % 10]

if and elif are mutually exclusive – only one block will run.
If num >= 100, then elif num >= 20: will be skipped, even if num was changed inside 
the if block.

'''

def convert_number_into_words(num):
    result = ""
    ones = ["", "one", "two", "three", "four", "five", "six",
            "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty",
            "seventy", "eighty", "ninty"]
    
    def convert_hundreds(num):
        word = ""

        if num >= 100:
            dig = num // 100
            word += ones[dig] + " hundred "
            num %= 100
            if num:
                word += " and "
            else:
                return word

        if num >= 20:
            dig1 = num // 10
            word += tens[dig1]
            if num % 10:
                word += "-" + ones[num % 10]
        elif num >= 10:
            word += teens[num - 10]
        elif num > 0:
            word += ones[num]

        return word


    if num >= 1000:
        quo = num // 1000
        result = result + ones[quo]
        num %= 1000
        if num:
            result += " thousand " + convert_hundreds(num)
    else:
        result = convert_hundreds(num)
    
    return result


number = 2234
res = convert_number_into_words(number)
print(res)
