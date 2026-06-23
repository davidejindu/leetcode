"""

open brackets must be closed by the same bracket

open brackets must be closed in correct order

using a stack

if these is not a stack and the bracket is closed we can return True since we cant open it

"""
class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')': '(', '}': '{', ']': '['}
        stack = []

        for bracket in s:
            if stack:
                if bracket in closeToOpen:
                    if stack[-1] != closeToOpen[bracket]:
                        return False
                    else:
                        stack.pop()

                else:
                    stack.append(bracket)

            else:
                if bracket in closeToOpen:
                    return False
                else:
                    stack.append(bracket)

        return not len(stack)
