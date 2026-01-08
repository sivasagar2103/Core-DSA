
'''
Greedy Algorithms:
A greedy algorithm is an approach for solving a problem by selecting the best 
option available at the moment. 
It doesn't worry whether the current best result 
will bring the overall optimal result.

If an optimal solution to the problem can be found by choosing 
the best choice at each step without reconsidering the 
previous steps once chosen, the problem can be solved using 
a greedy approach. This property is called greedy choice property.

'''

def assign_cookies(g, s):
    s.sort()
    g.sort()

    g_i = 0
    s_j = 0

    while g_i < len(g) and s_j < len(s):
        if s[s_j] >= g[g_i]:
            g_i += 1
        s_j += 1
    
    return g_i


g = [1,2]
s = [1,2,3]
#g = [1,2,3] #greed factor : which is the
            #minimum size of a cookie that the child will be content with
#s = [1,1] #each cookie j has a size s[j]
res = assign_cookies(g, s)
print(res)