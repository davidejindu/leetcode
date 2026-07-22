"""
pacific ocean touches the islands left and top edges
atlantic ocean touches the islands right and bottom edges

the value in each cell represents the height above sea level 

the water can flow neighboring cells if the neighboring cells are less or equal to the current cell height

return a 2D list of coordinates that water can flow from the cell, both atlantic and pacific oceans

input: [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
output: [0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]

first thing is we want to have a set where we store the coordinates of where water can flow from

we know that we can loop the top and left and all of those are pacific
then we know that we can loop the bottom and right and those are all atlantic 

then starting at each of those directions we want to see if neighboring cells are less than or equal to the current cell if it is we can go to that cell and add it to the set it correlates too


when we have all the coordinates for atlantic and pacific we will append whatever coordinates appear in both sets to the result

"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl, pacif = set(), set()
        result = []

        def dfs(r,c, height, store):
            if (r >= ROWS or 0 > r or
                c >= COLS or 0 > c or
                heights[r][c] < height or
                (r,c) in store):
                return

            store.add((r,c))

            dfs(r+1,c,heights[r][c], store)
            dfs(r-1,c,heights[r][c], store)
            dfs(r,c+1,heights[r][c], store)
            dfs(r,c-1,heights[r][c], store)

        for r in range(ROWS):
            dfs(r,0,heights[r][0],pacif)
            dfs(r,COLS-1,heights[r][COLS-1],atl)


        for c in range(COLS):
            dfs(0,c,heights[0][c],pacif)
            dfs(ROWS-1,c,heights[ROWS-1][c],atl)


        for r,c in atl:
            if (r,c) in pacif:
                result.append([r,c])

        return result

            

            

        