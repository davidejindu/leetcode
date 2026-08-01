"""

find two lines such that the can contain the most water

return the max water a container can store

the max water a container can store in the min height of the two lengths * distance apart
have two pointers and do that
move pointer to whatever heigh is smaller so you can keep max of the two lines



"""
class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxx = 0
        l, r = 0, len(height) - 1

        while l < r:
            minHeight = min(height[l], height[r])

            current_height = (r - l) * minHeight

            maxx = max(current_height, maxx)

            if height[l] < height[r]:
                l +=1
            else:
                r -=1

        return maxx

        
        