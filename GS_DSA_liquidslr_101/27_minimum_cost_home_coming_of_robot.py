'''
Problem Statement:
- An m * n grid
- Start position startPos = [sr, sc]
- Home position homePos = [hr, hc]
- Movement costs:
  . Moving into row r costs rowCosts[r]
  . Moving into column c costs colCosts[c]
- The robot can move up, down, left, or right, staying within bounds.
- Return the minimum cost to reach home.

Note:
- Any valid path from start to home that moves the required number 
  of rows and columns will have the same total cost.
- Order of moves does not matter

Approach Used: Greedy

Core Idea:
- To reach (hr, hc) from (sr, sc):
  - You must move vertically from sr → hr
  - You must move horizontally from sc → hc
- Each move cost depends only on the row or column you enter, not on the path.
- Therefore,
  - Sum the costs of all rows you enter while moving vertically
  - Sum the costs of all columns you enter while moving horizontally

- Greedy / Direct Summation
  . Move row by row from sr to hr (vertically)
  . Move column by column from sc to hc (horizontally)
  . Accumulate costs accordingly

Time: O(|sr − hr| + |sc − hc|)
Space: O(1)

'''
def min_cost(start, home, row_cost, col_cost):
    sr, sc = start
    hr, hc = home
    cost = 0

    #vertical
    if sr < hr:
        for i in range(sr+1, hr+1):
            cost += row_cost[i]
    else:
        for i in range(sr-1, hr-1, -1):
            cost += row_cost[i]

    if sc < hc:
        for i in range(sc+1, hc+1):
            cost += col_cost[i]

    else:
        for i in range(sc-1, hc-1, -1):
            cost += col_cost[i]
    return cost

startPos = [1, 0]
homePos  = [2, 3]
rowCosts = [5, 4, 3]
colCosts = [8, 2, 6, 7]
res = min_cost(startPos, homePos, rowCosts, colCosts)
print(res)
#3 + 2 + 6 + 7 = 18
'''
Vertical moves

Enter row 2 → cost rowCosts[2] = 3

Horizontal moves

Enter column 1 → cost 2

Enter column 2 → cost 6

Enter column 3 → cost 7


'''

