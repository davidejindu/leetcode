class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(path.copy()))
                return

            if openN < n:
                path.append("(")
                backtrack(openN + 1, closedN)
                path.pop()

            if closedN < openN:
                path.append(")")
                backtrack(openN, closedN + 1)
                path.pop()

            
        backtrack(0,0)
        return result

