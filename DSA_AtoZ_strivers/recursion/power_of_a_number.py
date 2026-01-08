#source: https://leetcode.com/problems/powx-n/description/
def power_of(num, index):

    def rec_pow(x, n):
        if n == 0:
            return 1
        
        temp = rec_pow(x, n // 2)

        if n % 2 == 0:
            return temp * temp
        else:
            return temp * temp * x

    if index < 0:
        num = 1/num
        index = -index
    
    return rec_pow(num, index)
    

number = 2
index = 2 #2
res = power_of(number, index)
print(res)