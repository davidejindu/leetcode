"""

determine if 9 * 9 sudoku board is valie

each row much contain digits 1-9 without repeat
each column much contain the digits 1-9 without repeat
each of the nine 3 * 3 boxed of grid must contain digits 1 - 9 without repeat

first start by checking duplicates in columns and rows
loop through each row and check if duplicates 

loop throguh each column and check if there are duplciates

have a hashmap where the key is the row and the value is a set of number
have a hashmap where the key is the col and the value is a set of number
have a hashmap where the key is the row/ 3 col /3 and the value is a set of number
if any number we iterate through is in one of these sets return False we have a duplicate

the squares hashmap is r / 3 c / 3 tuple because the squares are 3 by 3



"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r //3, c //3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True
        