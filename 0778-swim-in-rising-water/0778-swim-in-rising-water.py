class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set([0,0])
        minHeap = [(grid[0][0], 0, 0)] #max height, r, c
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROW, COL = len(grid), len(grid)


        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == ROW -  1 and c == COL -  1:
                return t

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (0 <= nr < ROW and
                    0 <= nc < COL and
                    (nr,nc) not in visited):
                    heapq.heappush(minHeap,(max(t,grid[nr][nc]), nr, nc))
                    visited.add((nr,nc))

            