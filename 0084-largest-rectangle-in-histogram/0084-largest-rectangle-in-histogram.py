class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """

        i want to check if the height is smaller than previous value
        if it is i have to pop the top value from stack because i can no longer extend it
        then i have to compute it to maxArea which is the height * the width
        then i have to give the height im on that index i popped because that means it was smaller so its valid for that index

        after i do that loop if the stack isnt empty that means the height can loop to end of heights so get the maxArea and return

        2,1,5,6,2,3

        maxArea = 0
        stack = []


        """

        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                start = index
                maxArea = max(maxArea, height * (i - index))

            stack.append((start, h))

        while stack:
            index, height = stack.pop()

            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea
