'''

Approach:
* Try all possible prefixes from the current position. 
  If the prefix is in the dictionary and the rest of the string 
  can be segmented similarly, we say segmentation is possible. 
  If no prefix works, segmentation is impossible.

what is the purpose of the below line?
* if prefix in words and find_words(i):
- This line tries every possible prefix starting at the current index.
- It confirms if the prefix is a dictionary word.
- If yes, it recursively checks whether the rest of the string can be segmented.
- Once a segmentation path leads to the end of the string, it returns True.
- If no valid segmentation is found for the prefix, it tries the next possible prefix.

Time: O(2 ** n * k ) -- k is the average length of substrings.
Space: O(n) -- recursion stack

'''

def word_break(sentence, words):
    n = len(sentence)

    def find_words(start):
        if start == n:
            return True
        
        for i in range(start+1, n+1):
            prefix = sentence[start : i]
            if prefix in words and find_words(i):
                return True
        return False

    return find_words(0)



s = "takeuforward"
words = ["take" , "forward" , "you", "u"]
res = word_break(s, words)
print(res)