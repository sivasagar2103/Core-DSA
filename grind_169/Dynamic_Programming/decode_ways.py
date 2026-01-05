'''

Space-optimized DP - Counting Only
- By using two variables
O(n)
O(1)
- decoding at index i only depends on i+1 and i+2.
- Scan from right to left
- If s[i] forms a valid 1-digit decode → add prev1
- If s[i:i+2] forms a valid 2-digit decode → add prev2
- Slide the window: (prev2, prev1) ← (prev1, curr)


DP + Pruned DFS
O(n + k·n)
O(n + k·n)

'''
def numDecodings_space_optimized(s):
    if not s or s[0] == '0':
        return 0

    n = len(s)
    prev1 = 1
    prev2 = 1

    for i in range(n - 1, -1, -1):
        curr = 0

        # Single digit decode
        if s[i] != '0':
            curr += prev1

        # Two digit decode
        if i + 1 < n:
            two = int(s[i:i+2])
            if 10 <= two <= 26:
                curr += prev2

        prev2, prev1 = prev1, curr

    return prev1

def decodeDPandPrint(s):
    n = len(s)
    if n == 0 or s[0] == '0':
        return 0, []

    # ---------- DP COUNT ----------
    dp = [0] * (n + 1)
    dp[n] = 1

    for i in range(n - 1, -1, -1):
        if s[i] != '0':
            dp[i] += dp[i + 1]
        if i + 1 < n:
            two = int(s[i:i+2])
            if 10 <= two <= 26:
                dp[i] += dp[i + 2]

    total_count = dp[0]
    if total_count == 0:
        return 0, []

    # ---------- DFS PRINT (PRUNED) ----------
    results = []

    def dfs(i, path):
        if i == n:
            results.append(path)
            return

        # 1-digit decode
        if s[i] != '0' and dp[i + 1] > 0:
            num = int(s[i])
            dfs(i + 1, path + chr(ord('A') + num - 1))

        # 2-digit decode
        if i + 1 < n:
            two = int(s[i:i+2])
            if 10 <= two <= 26 and dp[i + 2] > 0:
                dfs(i + 2, path + chr(ord('A') + two - 1))

    dfs(0, "")

    return total_count, results


def decodeCombinations(s):
    results = []
    n = len(s)
    cons = ord('A')
    
    def dfs(i, path):
        if i == n:
            results.append(path)
            return
        
        # 1-digit decode
        if s[i] != '0':
            num = int(s[i])
            dfs(i + 1, path + chr(cons + num - 1))

        # 2-digit decode
        if i + 1 < n:
            num = int(s[i:i+2])
            if 10 <= num <= 26:
                dfs(i + 2, path + chr(cons + num - 1))

    dfs(0, "")
    return results


s = "226"
res = numDecodings_space_optimized(s)
print(res)
result = decodeDPandPrint(s)
print(result)
r1 = decodeCombinations(s)
print(r1)
