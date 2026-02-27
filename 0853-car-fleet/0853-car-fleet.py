class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
    so we can get the time itll take to reach the position by doing
    (target - postion) / speed
    we can create an array of pairs where we zip ang get the positon and speed
    the we can sort it in reversing order and append the value to stack
    if the stack is greater than len 2 then we can compare it the top to the second val
    if the second val is faster or greater that means it catches up but
    so itll be a fleet meaning we will pop it



        """

        pairs = [[p, s] for p, s in zip(position,speed)]
        stack = []

        for p, s in sorted(pairs)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)