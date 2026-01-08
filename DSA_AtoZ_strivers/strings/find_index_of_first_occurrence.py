'''
* Naive or Brute or Basic Approach:

- Tries all positions, restarts on mismatch.
- Time Complexity	Worst: O(n x m)
- Space Complexity	O(1)
- Backtracking

* Knuth-Morris-Pratt Algorithm [KMP]:
- KMP improves over brute force by avoiding redundant comparisons
using a preprocessed pattern table (LPS array or pi table: Longest Prefix which is also suffix)

- Time complexity: O(n + m)
- space complexity: O(m) - for LSP array
- Preprocesses pattern to skip re-checks
- No backtracking
- Always linear regardless of input

'''

def find_index(string, pattern):

    def build_lps(pattern):
        n = len(pattern)
        lps = [0] * n
        start = 0

        i = 1

        while i < n:
            if pattern[i] == pattern[start]:
                start += 1
                lps[i] = start
                i += 1
            else:
                if start > 0:
                    start = lps[start - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = build_lps(pattern)
    i = j = 0

    while i < len(string):
        if string[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(needle):
                return i - j
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1

haystack = "sagarsadbutbad"
needle = "sad"
res = find_index(haystack, needle)
print(res)
