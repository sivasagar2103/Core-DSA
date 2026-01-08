def word_search(board, word):
    nrows = len(board)
    ncols = len(board[0])
    word_length = len(word)
    diff_row = [-1,0,1,0]
    diff_col = [0,1,0,-1]
    seen = [[False for _ in range(ncols)] for _ in range(nrows)]

    #pre process and break the invalid input board and word by using ferequency method
    def pre_check_frequency():
        board_char_freq = {}
        word_char_freq = {}

        for i in range(nrows):
            for j in range(ncols):
                char = board[i][j]
                if char not in board_char_freq:
                    board_char_freq[char] = 0
                board_char_freq[char] += 1
        
        for char in word:
            if char not in word_char_freq:
                word_char_freq[char] = 0
            word_char_freq[char] += 1
        
        for word_char in word:
            if word_char not in board_char_freq or word_char_freq[word_char] > board_char_freq[word_char]:
                return False

        return True
    
    if not pre_check_frequency():
        return False
    
    #Reverse the string if the count of first character is greater than the last character
    '''
    If the starting letter is very common, 
    we waste time starting from many positions that go nowhere.
    If we reverse the word and start from a rarer letter,
    there are fewer possible starting points — fewer recursive calls,
    faster fail, and less backtracking.
    Say the board has:
    A 15 times
    D (last character) only 1 time
    If word = "ABCD":
    We’ll try to match "A" in 15 places — only one might work.
    If we reverse the word to "DCBA", we start from only 1 place (where D is),
    which is much more efficient.
    '''

    first_char, last_char = word[0], word[-1]
    first_count, last_count = 0, 0
    for r in range(nrows):
        for c in range(ncols):
            if board[r][c] == first_char:
                first_count += 1
            elif board[r][c] == last_char:
                last_count += 1
    if first_count > 0 and last_count > 0 and first_count > last_count:
        word = word[::-1]
                
    #recursion and backtracking
    def backtrack(sr, sc, char_index):
        if char_index == word_length:
            return True
        if sr < 0 or sr >= nrows or sc < 0 or sc >= ncols or board[sr][sc] != word[char_index]:
            return False
        seen[sr][sc] = True
        for i in range(4):
            neighbour_row = sr + diff_row[i]
            neighbour_col = sc + diff_col[i]
            if backtrack(neighbour_row, neighbour_col, char_index + 1):
                return True
        return False
    
    for i in range(nrows):
        for j in range(ncols):
            if backtrack(i, j, 0):
                return True
    
    return False



# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
result = word_search(board, word)
print(result)