class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        """
    while stack and the current temperature is greater than stack 
    pop the stack and add i - stackindex to the result array

        73,74,75,71,69,72,76,73
        [0,0,0,0,0,0,0,0]
        stack = [(0,73), ]
        """

        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackIndex, stackTemp = stack.pop()
                result[stackIndex] = i - stackIndex

            stack.append([i, temp])

        return result