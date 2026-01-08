'''


'''

def can_complete_bf(gas, cost):

    '''
    Time : O(n**2)
    
    '''

    n = len(gas)

    for start in range(n):
        tank = 0
        valid = True
        for step in range(n):
            i = (start + step) % n # %n is for circular behavior
            tank += gas[i] - cost[i]
            if tank < 0:
                valid = False
                break
        
        if valid:
            return start
        
    return -1

def can_complete_prefix(gas, cost):
    n = len(cost)
    gain = [gas[i] - cost[i] for i in range(n)]
    print(gain)

    if sum(gain) < 0:
        return -1
    
    total = 0
    min_sum = gain[0]
    min_index = 0

    for i in range(n):
        total += gain[i]
        print(total)
        if total < min_sum:
            min_sum = total
            min_index = i

    return (min_index + 1) % n


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
#Output: 3
res = can_complete_bf(gas, cost)
print(res)

result = can_complete_prefix(gas, cost)
print(result)