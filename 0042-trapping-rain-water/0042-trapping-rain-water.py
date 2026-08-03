"""


to get how much is trapped you need to get the min of max l and max r pointer

0,1,0,2,1,0,1,3,2,1,2,1
    l           
                      r

maxLeft = 
maxRight = 1
water = 0
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = maxRight = 0
        water = 0
        l, r = 0, len(height) - 1

        while l < r:
            
            if height[l] <= height[r]:
                maxLeft = max(height[l], maxLeft)

                if maxLeft - height[l] > 0:
                    water += maxLeft - height[l]

                l +=1

            
            else:
                maxRight = max(height[r], maxRight)

                if maxRight - height[r] > 0:
                    water += maxRight - height[r]

                r -=1

        return water
            
        