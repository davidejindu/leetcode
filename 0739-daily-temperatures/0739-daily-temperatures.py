class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                i, temp = stack.pop()
                result[i] = index - i

            stack.append((index, temperature))

        return result
        