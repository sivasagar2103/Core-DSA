'''
"Expand Around Center" technique
Intuition:
- A palindrome mirrors around its center.
- The center of a palindrome can be:
  . A single character (for odd-length palindromes, e.g., "aba")
  . Between two characters (for even-length palindromes, e.g., "abba")
- For each position in the string, we try to expand outwards around these
  two possible centers and check how far we can go while characters on both sides are equal.

Approach:
- Initialize variables
  . start = starting index of the longest palindrome found so far.
  . max_len = length of the longest palindrome found so far, initially 1
- Loop through each character as center candidate
- Check for odd-length palindrome centered at i

Note: For each character, exapnd outwards as long as characters macth, that requires O(N)
steps per center, leads to O(N**2).

Time: O(N**2)
Space: O(1)

Manacher's Algorithm
Core Idea:
- Leverage previously computed results by mirroring about center C whenever possible.
- Expand only where needed, reducing unnecessary checks.
- Update your tracking center and boundary as you find bigger palindromes.

steps:
- Preprocessing with Separators
  . odd and even length palindromic substrings become structurally identical
  (all have odd lengths)
- Mirroring and Reusing Information
  . For each center position i, if it falls within the current known rightmost palindrome
  (i < right), the algorithm knows that the plaindrome at the mirror position (2*center - i)
  can provide the lower bound to start its expansion at i.
  . mirroring means skipping the most expansions, as we already known the substring within
  the boundary is a plaindrome.
- Tracking and Advancing Right Boundary
  . Each successful comparison results in right moving one step forward, and it never
    reduces, i.e., the inner while loop gets executed at most n times.

Time: O(n)
Space: O(n)

'''


def longest_palindrome_substring(sen):
    n = len(sen)
    start = 0
    max_length = 1

    for i in range(n):
        # Odd length palindrome (center at i)
        l, r = i, i
        while l >= 0 and r < n and sen[l] == sen[r]:
            curr_length = r-l +1
            if curr_length > max_length:
                start, max_length = l, curr_length
            l -= 1
            r += 1
        
        # Even length palindrome (center between i and i+1)
        l, r = i, i+1
        while l >= 0 and r < n and sen[l] == sen[r]:
            curr_length = r-l +1
            if curr_length > max_length:
                start, max_length = l, curr_length
            l -= 1
            r += 1
    
    return sen[start: start + max_length]


def macher_algorithm(sen):
    #to handle even-length palindromes
    t_sen = '#' + '#'.join(sen) + '#'
    n = len(t_sen)
    p = [0] * n #stores the radius of the palindrome centered at i
    center = 0 #center of the current rightmost palindrome
    right = 0 #right boundary of the palindrome
    center_index = 0
    max_length = 0

    for i in range(n):
        #mirror trick
        '''
        If 'i' is inside the current rightmost palindrome then we 
        already know the minimum possible palindrome length - by symmetry(mirror)
        about center. [to the left of right]

        '''
        mirror = 2* center -1
        if mirror < right:
            p[i] = min(right-i, p[mirror])
        else:
            p[i] = 0
          
        a = i + p[i] + 1
        b = i - p[i] - 1

        '''
        grow the palindrome outward by comparing characters at the new edges (a and b)
        from the current center
        '''
        while a < n and b >= 0 and t_sen[a] == t_sen[b]:
            p[i] += 1
            a += 1
            b -= 1
        
        '''
        If palindrome at i goes beyond current right, you have a new rightmost
        palindrome. Update center and right accordingly.
        '''
        if i + p[i] > right:
            center = i
            right = i + p[i]
        
        if p[i] > max_length:
            max_length = p[i]
            center_index = i
    
    start = (center_index - max_length)//2
    return sen[start : start+max_length]

s = "babad"
res = macher_algorithm(s)
print(res)