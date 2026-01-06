def find_quadrant(x, y):
    if x == 0 and y == 0:
        return "origin"
    elif x == 0:
        return 'y-axis'
    elif y == 0:
        return 'x-axis'
    elif x > 0 and y > 0:
        return "Q1"
    elif x < 0 and y > 0:
        return "Q2"
    elif x < 0 and y < 0:
        return "Q3"
    elif x > 0 and y < 0:
        return "Q4"

x = 0
y = 5
res = find_quadrant(x, y)
print(res)