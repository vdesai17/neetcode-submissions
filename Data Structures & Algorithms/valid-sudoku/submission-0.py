class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #1. each row must contain digits 1-9 without duplicates
        #2. each col must contain digits 1-9 w/o duplicates
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_set or board[i][j] == 0:
                        return False
                    row_set.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in col_set or board[j][i] == 0:
                        return False
                    col_set.add(board[j][i])
        
        #3. each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
        squares = collections.defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                
                if board[row][col] in squares[(row // 3, col // 3)]:
                    return False
                squares[(row // 3, col // 3)].add(board[row][col])
                
        return True