
def lemonade_change(nums):
    five, ten = 0, 0

    for num in nums:
        if num == 5:
            five += 1
        elif num == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True
        


bills = [5,5,5,10,20]
#bills = [5,5,10,10,20]
res = lemonade_change(bills)
print(res)