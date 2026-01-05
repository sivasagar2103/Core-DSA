'''
Core Idea:
If the total gas is less than the total cost, completing the circuit is impossible.
Otherwise, there exists exactly one valid starting station.
Track a running fuel balance and reset the start whenever the tank goes negative.

Steps of implementation:
1. Initialize:
   - total = 0 (net gas across all stations)
   - tank = 0 (current fuel balance)
   - start = 0 (candidate starting index)
2. Traverse all stations from left to right:
   - Compute gain = gas[i] - cost[i].
   - Add gain to total and tank.
3. If tank becomes negative at station i:
   - Starting anywhere from current start to i is invalid.
   - Reset start = i + 1.
   - Reset tank = 0.
4. After traversal:
   - If total >= 0:
     . Return start (valid starting station).
   - Else:
     . Return -1 (no solution).

Time: O(n)
Space: O(1)

“If total gas < total cost → impossible.
If tank drops below zero → reset start.”

Out Of Scope:

Q: Why There Is Only ONE Valid Starting Point?
A: If a start point fails at some station (negative tank at index i),
   every index between those points  would also fail, 
   so they cannot be valid starting points. 
   Therefore, the solution is unique.

Variants:
| Variation                   | Description                    | Approach                      |
| --------------------------- | ------------------------------ | ----------------------------- |
| Find all valid starts       | Return every possible start    | Prefix sum + minimum tracking |
| Max fuel left over          | Optimize remaining fuel        | Simulate from valid start     |
| Minimum refueling stops     | Stations with fuel & distances | Max-heap greedy               |
| Linear route (not circular) | No wrap-around                 | Priority queue                |

'''

def complete_circuit(gas, cost):
    n = len(gas)
    total = 0
    tank = 0
    start = 0

    for i in range(n):
        gain = gas[i] - cost[i]
        total += gain
        tank += gain

        if tank < 0:
            start = i + 1
            tank = 0
    
    return start if total >= 0 else -1


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
res = complete_circuit(gas, cost)
print(res)
