class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        """
        dfs 
        if grid[m][n] == 1 
        increment num of islands
        make all the areas around it 0 so it doesnt count as another island

        """
        
        row, column = len(grid), len(grid[0])
        def dfs(i,j):

            if i >= row or i < 0 or j >= column or j < 0 or grid[i][j] == "0":
                return

            

            else:
                grid[i][j] = "0"
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)

        num_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_of_islands +=1
                    dfs(i,j)

        return num_of_islands
