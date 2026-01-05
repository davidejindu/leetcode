class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        maximumArea = 0

        while l < r:
            distance = r - l

            if height[l] < height[r]:
                maximumArea = max(maximumArea,distance * height[l])

            else:
                maximumArea = max(maximumArea, distance * height[r])

            if height[l] < height[r]:
                l+=1

            else:
                r -=1

        return maximumArea