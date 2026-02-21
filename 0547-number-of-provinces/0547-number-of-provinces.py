class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """

[
    [1,1,0],
    [1,1,0],
    [0,0,1]
    ]

    visited(0,1,)
        """

        visited = set()
        providence = 0

        def dfs(i):
            visited.add(i)

            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)
            return


        for i in range(len(isConnected)):
            if i not in visited:
                providence +=1
                dfs(i)

        return providence
