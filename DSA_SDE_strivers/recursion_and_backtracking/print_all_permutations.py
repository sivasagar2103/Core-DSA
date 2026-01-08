'''
* Find All Permutations
Steps:
1. Recursion on Position:
- start = 0
- At each recursion level, fix one character at the current start index.

2. Swapping:
- Swap the character at start with the character at i (where i ranges from start to n-1).
- This places a new candidate character at the current fix position.

3. Recursive Call:
- After the swap, move to the next index (start + 1) by recursively calling the same function.

4. Base Case:
- when start == n , collect the result

5. Backtracking (Swap Back):
- Restore the original order before the next candidate swap is tried.

Summary:
- Fix one character at each position by swapping.
- Recurse and repeat for the next position.
- Swap back after recursion to restore state (backtracking).
- Base case collects a permutation when all positions are fixed.

Time: 
Total permutations: n!
Work per permutation: n
Total : O(n * n!)

Space:
- Recursive Stack: O(n)
- Result Storage: O(n * n!)
Total : O(n) + O(n*n!)


* Find Unique Permutations

Steps:
1. Sort the input list
2. Intialize seen and result
3. Recursive Function
4. Base Condition

Time: O(n * n!)
Space:
O(n) - recursive space
O(n * m) - m is the number of unique permutations generated.

Note:
- Backtracking here is a depth-first search through a state space tree, where:
  . Each node represents a partial permutation.
  . Branches represent choosing the next character that hasn't been used yet.
- Duplicate pruning avoids exploring branches symmetric due to repeated characters.
- The recursion explores all valid unique permutations by incrementally building 
  candidate paths and abandoning invalid or duplicate ones early.

'''

def find_permutations(word):
    n = len(word)
    result = []


    def permutations(start):
        if start == n:
            result.append(''.join(word))
            return
        
        for i in range(start, n):
            word[i], word[start] = word[start], word[i]
            permutations(i+1)
            word[i], word[start] = word[start], word[i]

    permutations(0)
    return result

def find_permutations_unique(word):
    word.sort()
    n = len(word)
    seen = [0] * n
    result = []

    def unique_permutations(path):
        if len(path) == n:
            result.append(''.join(path[:]))
            return
        
        for i in range(n):
            if seen[i]:
                continue

            if i > 0 and word[i-1] == word[i] and not seen[i-1]:
                continue 

            seen[i] = 1
            path.append(word[i])
            unique_permutations(path)
            path.pop()
            seen[i] = 0
    
    unique_permutations([])
    return result


s = "abc"
res = find_permutations(list(s))
print(res)
#Output: ["abc","acb","bac","bca","cab","cba"]

s2 = "aab"
res2 = find_permutations_unique(list(s2))
print(res2)
#['aab', 'aba', 'baa']
