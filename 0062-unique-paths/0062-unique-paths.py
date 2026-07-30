class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def paths(r, c):
            if r == m or c == n:
                return 0

            if r == m - 1 and c == n - 1:
                return 1

            if (r,c) in memo:
                return memo[(r,c)]

            memo[(r,c)] = paths(r+1,c) + paths(r, c + 1)

            return memo[(r,c)]

        return paths(0,0)