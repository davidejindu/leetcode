class Solution:
    def isValid(self, s: str) -> bool:
        """
        so create a hashmap linking close to open
        check if the current value is closed or open
        if it is closed check if the top of stack matches open version
        if not return false because its a closed bracket or incompatiable
        else pop to the stack


        """

        closeToOpen = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for bracket in s:
            if bracket in closeToOpen:
                if stack and closeToOpen[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return not stack