#valid sudoku
#https://leetcode.com/problems/valid-sudoku/
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        rows=board
        cols=zip(*board)
        squares=[]
        for i in [0,1,2]:
            for j in [0,1,2]:
                t=[]
                t.extend(rows[i*3][j*3:j*3+3])
                t.extend(rows[i*3+1][j*3:j*3+3])
                t.extend(rows[i*3+2][j*3:j*3+3])
                squares.append(t)
        for lists in [rows,cols,squares]:
            for list in lists:
                test=''.join(list).replace(".","")
                if len(set(test)) != len(test):
                    return False
        return True
board=[
    "53..7....",
    "6..195...",
    ".98....6.",
    "8...6...3",
    "4..8.3..1",
    "7...2...6",
    ".6....28.",
    "...419..5",
    "....8..79"
]
# board=["..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."]
# board = ["......5..",".........",".........","93..2.4..","..7...3..",".........","...34....",".....3...",".....52.."]
s=Solution()
print s.isValidSudoku(board)
