"""
open brackets must be closed by the same type of brackets

open brackets must be closed in the correct order

close brackets must have a corresponding open bracket

if the next string is a closed bracket and it doesnt match the top of stack with open
bracket we know its false

if the stack is empty and it is a close bracket we know its false

after the loop we return not len(stack) meaning stack is true if its empty because everything succesfully closed

have a map 


"""
class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')': '(', '}': '{', ']': '['}
        stack = []

        for bracket in s:
            if stack:
                if bracket in closeToOpen:
                    if closeToOpen[bracket] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(bracket)

            else:
                if bracket in closeToOpen:
                    return False
                else:
                    stack.append(bracket)

        return not len(stack)

        