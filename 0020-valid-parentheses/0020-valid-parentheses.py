class Solution:
    def isValid(self, s: str) -> bool:
        
        openToClose = {")": "(", "]": "[", "}": "{"}
        stack = []

        for bracket in s:
            if bracket in openToClose:
                if stack and openToClose[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return not stack