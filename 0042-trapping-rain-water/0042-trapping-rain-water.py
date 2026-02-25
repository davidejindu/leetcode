class Solution:
    def trap(self, height: List[int]) -> int:
        """

l                       
0,1,0,2,1,0,1,3,2,1,2,1
                      r

 
two pointers get the minimum of the max of right and left
then do min(maxright,maxleft) - height[i] if its greater
than 0 add to result
this means that there is a wall to the left and if you add water it will get
trapped in i



        """

        if not height: return 0
        """
                  l                       
    0,1,0,2,1,0,1,3,2,1,2,1
                r
    leftMax = 3
    rightMax = 2
    result = 6

        """
        l, r = 0, len(height) - 1
        result = 0
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if rightMax < leftMax:
                r -=1
                if rightMax - height[r] > 0:
                    result += rightMax - height[r]
                rightMax = max(rightMax, height[r])

            else:
                l +=1 
                if leftMax - height[l] > 0:
                    result += leftMax - height[l]

                leftMax = max(leftMax, height[l])

        return result