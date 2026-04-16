class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        result = []
        directions = [[1,0], [-1,0], [0,1], [0,-1]]


        def dfs(r,c,visit,prevHeight):
            visit.add((r,c))

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if(0 <= nr < ROW and 
                   0 <= nc < COL and
                   (nr,nc) not in visit and
                   prevHeight <= heights[nr][nc]):
                   dfs(nr,nc,visit,heights[nr][nc])

        for r in range(ROW):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,COL - 1,atlantic,heights[r][COL - 1])
            

        for c in range(COL):
            dfs(0,c,pacific,heights[0][c])
            dfs(ROW - 1,c,atlantic,heights[ROW - 1][c])


        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append((r,c))

        return result





