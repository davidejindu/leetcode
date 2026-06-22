
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxHeight = 0
        l,r = 0, len(height) - 1

        while l < r:
            width = r - l 
            minHeight = min(height[l], height[r]) 

            maxHeight = max(maxHeight, minHeight * width)

            if height[l] < height[r]:
                l +=1
            else:
                r -=1

        return maxHeight
        