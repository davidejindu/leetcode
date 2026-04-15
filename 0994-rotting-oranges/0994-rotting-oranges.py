class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        queue = deque()
        fresh = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh +=1
    


        minutes = 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    r, c = dr+ row, dc + col
                    if (0 <= r < ROW and 
                        0 <= c < COL and
                        (r,c) not in visited and
                        grid[r][c] == 1
                        ):
                            queue.append((r,c))
                            visited.add((r,c))
                            fresh -=1

            minutes +=1

        return minutes if fresh == 0 else -1

