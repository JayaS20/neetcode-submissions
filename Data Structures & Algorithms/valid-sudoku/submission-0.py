class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seenRow = set()
            for nums in row:
                if nums == ".":
                    continue
                if nums in seenRow:
                    return False
                seenRow.add(nums)
        for col in range(9):
            seenCol = set()
            for row in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if num in seenCol:
                    return False
                seenCol.add(num)
        
        for board_row in range(0, 9, 3):
            for board_col in range(0, 9, 3):
                seen = set()
                for r in range(board_row, board_row+3):
                    for c in range(board_col, board_col+3):

                        num = board[r][c]

                        if num == ".":
                            continue
                        if num in seen:
                            return False
                        seen.add(num)
        return True
