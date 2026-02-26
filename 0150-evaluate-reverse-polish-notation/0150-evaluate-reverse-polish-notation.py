import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        """
        make stack 
        loop through it if you get one of the operators
        check if result = float('inf')
        if true pop stack twice. the first will be second val the second pop is first val
        the do first value operator second value and add to result

        "10","6","9","3","+","-11","*","/","*","17","+","5","+"
                                                     ^                         
         stack = []
         don't need a result just stack
         if char in operator:
            second_val = stack.pop()
            first_val = stack.pop()
            result = first_val operator second_val
            else:
                val = stack.pop()
                result = val operator result
        """

        stack = []
        for token in tokens:
            if token == "+":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b + a))
            elif token == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b - a))
            elif token == "*":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b * a))
            elif token == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b /a))
            else:
                stack.append(int(token))
                
        return stack[0]
