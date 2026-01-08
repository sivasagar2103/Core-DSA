'''

Recusrion:
- Recursion is a programming technique where a function calls itself 
  to solve a smaller instance of the same problem.
- Each recursive call adds a new layer to the call stack until a 
  base case is reached, at which point the stack unwinds.

Backtracking:
- Backtracking is a systematic way to iterate through all possible configurations
  of a problem by building a solution incrementally and abandoning a path as soon as
  it is determined it cannot possibly lead to a valid solution.
- Relies on recursion to explore decision trees.
Working Steps:
- You choose an option and move forward (recursive call).
- At each step, you check:
  . If the current path is a solution, save it.
  . If not, explore further by recursive decisions.
  . When a path proves invalid or complete, you “backtrack”: 
    undo the last step(s) and try alternative choices.
- Continue until all possibilities are explored.

Summary:
- Recursion is self-calling to solve subproblems.
- Backtracking is recursion plus "undoing" choices to explore 
  all possible solutions systematically
- Backtracking uses Brute-Force Approach[says try out all 
   possible solutions and pick desired solution].
- Backtracking is used when you have multiple solutions and want all those solutions.

- Dynamic Programming is used for optimizations problems.
'''

def find_subsets_of_nums_bf(arr):
    '''
    - Duplicate check costly (temp not in result)
    - Time: O(n * 2**n)
    - Space: O(n* 2**n)
    
    '''


    result = [[]]
    for num in arr:
        sub_set = []
        for element in result:
            temp = element + [num]
            if temp not in result:
                sub_set.append(temp)
        result += sub_set

    return result


def find_subsets_of_nums_bt(arr):
    '''
    - Sort the input list to group duplicates together.
    - Recursion to explore each subset:
      . At each recursion level, either include or exclude the current element.
      . Skip duplicate elements at the same recursion depth
    - Add the current subset to the result at every recursive call.
    - Use backtracking (append + recursive call + pop) to build subsets incrementally 
      and revert choices to explore all possible unique subsets.
    - Time: 
      . 2**n for finding all the subsets
      . n for copying subsets to the result 
      . Total : O(n * 2 ** n)
    - Space:
      . Recursion Stack - O(n)
      . Result List - O(n * 2**n)
      . Total : O(n * 2 ** n)

    '''
    arr.sort()
    res = []
    n = len(arr)

    def back_track(start, path):
        res.append(path[:])
        for i in range(start, n):
            if i > start and arr[i] == arr[i-1]:
                continue
            path.append(arr[i])
            back_track(i+1, path)
            path.pop()

    back_track(0, [])
    return res

nums = [1, 2, 2]
res = find_subsets_of_nums_bt(nums)
print(res)