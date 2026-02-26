class Solution:
    def isValid(self, s: str) -> bool:

        """
        the top of the stack has to be a open bracket
        you want to create a hashmap where its closed to open
        if the stack isnt empty and character in s is closed bracket and the top
        of the bracket isn't the open versionyou return False 

        if the bracket is open keep appending it to the stack

        after the for loop if stack isn't empty return false else return true
        since it should be empty if everything was popped
        
        """

        stack = []
        closeToOpen = {")" : "(", "}": "{", "]": "["}

        for char in s:
            if char in closeToOpen:
                if stack and closeToOpen[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        
        if not stack: 
            return True 

        else: return False

        

        