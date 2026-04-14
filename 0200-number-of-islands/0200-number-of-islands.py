class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0 

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]

        def dfs(r,c): 
            visited.add((r,c))

            for dr, dc in directions:
                nei_row, nei_col = r + dr, c + dc

                if (0 <= nei_row < ROWS and 0 <= nei_col < COLS and
                    (nei_row, nei_col) not in visited and grid[nei_row][nei_col] == "1"):
                    dfs(nei_row, nei_col)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands +=1

        return islands

