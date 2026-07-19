"""
going to see if word exists in grid

backtrack 

if i == len word return tru

have a set to keep places you've already visited

keep if the current word builder index is same value as word index




"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        def backtrack(r, c, i, currentWord):
            if i == len(word):
                return True

            if (0 > r or r >= ROWS or
                0 > c or c >= COLS or
                (r,c) in visited or
                board[r][c] != word[i]):
                return

            visited.add((r,c))
            currentWord += board[r][c]

            result = (backtrack(r + 1, c, i + 1, currentWord) or
                    backtrack(r, c - 1, i + 1, currentWord) or
                    backtrack(r, c + 1, i + 1, currentWord) or 
                    backtrack(r - 1, c, i + 1, currentWord))

            visited.remove((r,c))

            return result
    
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r,c,0, ""):
                    return True

        return False
    