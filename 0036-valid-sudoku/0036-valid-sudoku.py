class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        create a hashmap that has a hashset as value
        for the hashmapa if the col or rows or squares in hashset return False
        keep traversing
        squares will be hashset key of r//3 c//3 
        this is because if row is 2 2/3 == 0 so its in first row

        """
        row_map = collections.defaultdict(set)
        col_map = collections.defaultdict(set)
        square_map = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in row_map[r] or board[r][c] in col_map[c] 
                    or board[r][c] in square_map[(r//3,c//3)]):

                    return False
                
                row_map[r].add(board[r][c])
                col_map[c].add(board[r][c])
                square_map[(r//3,c//3)].add(board[r][c])

        return True