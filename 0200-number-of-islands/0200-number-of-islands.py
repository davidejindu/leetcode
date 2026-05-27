class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        can just dfs and check if the r c is in range and then check if its 1
        if its 1 mark it as visited
        the goal is to mark the neighboring 1's as visited in dfs so you dont revisit it



        """
        visited = set()
        ROW, COL = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        islands = 0

        def dfs(r,c):
            visited.add((r,c))

            for dr,dc in directions:
                nr, nc = dr + r, dc + c

                if (0 <= nr and nr < ROW and
                    0 <= nc and nc < COL and
                    (nr,nc) not in visited and
                    grid[nr][nc] == "1"):
                    dfs(nr,nc)



        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] =="1" and (r,c) not in visited:
                    islands +=1
                    dfs(r,c)

        return islands
