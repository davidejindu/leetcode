class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        ROW, COL = len(board), len(board[0])
        path = set()


        def dfs(i,r,c):
            if i == len(word):
                return True

            if(0 > r or r >= ROW or
               0 > c or c >= COL or
               (r,c) in path or
               board[r][c] != word[i]):
               return False

            path.add((r,c))

            result = (dfs(i+1,r +1,c) or
                      dfs(i+1,r -1,c) or
                      dfs(i+1,r,c +1) or
                      dfs(i+1,r,c-1))

            path.remove((r,c))
            return result


        for r in range(ROW):
            for c in range(COL):
                if dfs(0,r,c):
                    return True

        return False