class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()


        def bfs(r, c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))

            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nei_row, nei_col = row + dr, col + dc

                    if (0 <= nei_row < ROWS and 0 <= nei_col < COLS and
                        (nei_row,nei_col) not in visited and grid[nei_row][nei_col] == "1"):
                        queue.append((nei_row, nei_col)) 
                        visited.add((nei_row, nei_col))







            




        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    islands +=1

        return islands

