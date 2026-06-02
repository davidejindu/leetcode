"""
pacific top and left
atlantic bottom and right

the value in cell is the height above seal level

if neighboring cell height is <= current cell water can flow

input grid

output is 2D list of grid coordinates result where result[i] = [row,col]
that water can flow from that cell to both pacific and atlantic oceans


so instead of looping through all the cells start looping through the pacific and atlantic ocean do a dfs and add all the cells that are greater than the prevheight

then check if there are r,c in both sets that match


"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r,c,visited,prevHeight):
            if (0 > r or r >= ROWS or
                0 > c or c >= COLS or
                (r,c) in visited or
                heights[r][c] < prevHeight):
                return

            visited.add((r,c))

            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])

        for c in range(COLS):
            dfs(0,c,pacific,heights[0][c])
            dfs(ROWS - 1,c,atlantic,heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,COLS - 1,atlantic,heights[r][COLS-1])


        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append((r,c))


        return result




        