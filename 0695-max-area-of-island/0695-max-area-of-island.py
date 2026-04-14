class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        same bfs approach instead of just counting visited need to count neighbors
        keep global variable maxAreaOfIsland

        have to make a inner loop inside the bfs

        """

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_island = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            area = 0

            while queue:
                area +=1
                row, col = queue.popleft()

                for dr, dc in directions:
                    nei_row, nei_col = dr + row, dc + col

                    if (0 <= nei_row < ROWS and 0 <= nei_col < COLS and
                        (nei_row,nei_col) not in visited and grid[nei_row][nei_col] == 1):
                        queue.append((nei_row,nei_col))
                        visited.add((nei_row,nei_col))

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_island = max(bfs(r,c), max_island)

        return max_island