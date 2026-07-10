class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            valid = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in valid:
                        return False
                    else:
                        valid.add(board[i][j])
        for j in range(9):
            valid = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in valid:
                        return False
                    else:
                        valid.add(board[i][j])
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                valid = set()
                for i in range(3):
                    for j in range(3):
                        if board[row+i][col+j] != ".":
                            if board[row+i][col+j] in valid:
                                return False
                            else:
                                valid.add(board[row+i][col+j])
        return True

