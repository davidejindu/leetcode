"""

so im thinking you have a stack and when you get an operand you pop from the stack twice
the so it looks like
second pop operand first pop
after you calculate that value you add it to the stack

string = [2,1,+,3,*]
stack = [9]


"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand = set()
        operand.add("+")
        operand.add("-")
        operand.add("/")
        operand.add("*")
        stack = []


        for val in tokens:
            if val not in operand:
                stack.append(val)

            else:
                second = stack.pop()
                first = stack.pop()
                if val == "+":
                    value = int(first) + int(second)
                    stack.append(value)
                elif val == "-":
                    value = int(first) - int(second)
                    stack.append(value)
                elif val == "/":
                    value = int(first) / int(second)
                    stack.append(value)
                else:
                    value = int(first) * int(second)
                    stack.append(value)

        return int(stack[0])
        