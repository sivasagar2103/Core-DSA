'''
Run-length encoding (RLE) is a string compression method that works by 
replacing consecutive identical characters (repeated 2 or more times) 
with the concatenation of the character and the number marking the count 
of the characters (length of the run). 
For example, to compress the string "3322251" we replace "33" with "23",
replace "222" with "32", replace "5" with "15" and replace "1" with "11". 
Thus the compressed string becomes "23321511"

Standard RLE:
Compress a given fixed string like:
Input: "AAABBB"
Output: "3A3B"

Count-and-Say:
It's a recursive sequence where:
countAndSay(1) = "1"
countAndSay(2) = "one 1" → "11"
countAndSay(3) = "two 1s" → "21"
countAndSay(4) = "one 2, one 1" → "1211"
countAndSay(5) = "one 1, one 2, two 1s" → "111221"

'''


def count_and_say(n):
    if n == 1:
        return "1"
    

    def rle_code(sen):
        result = []
        i = 0
        while i < len(sen):
            count = 1
            while i + 1 < len(sen) and sen[i] == sen[i+1]:
                count += 1
                i += 1
            result.append(str(count) + sen[i])
            i += 1
        return ''.join(result)


    current = "1"
    for i in range(1, n):
        current = rle_code(current)

    return current 


n = 4
res = count_and_say(n)
print(res)