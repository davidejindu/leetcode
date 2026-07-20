class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()


        def dfs(r,c):
            if (0 > r or r >= ROWS or
                0 > c or c >= COLS or
                grid[r][c] != "1" or
                (r,c) in visited):
                return

            visited.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands +=1
                    dfs(r,c)


        return islands
        