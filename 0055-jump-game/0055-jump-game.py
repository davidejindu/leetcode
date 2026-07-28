"""

each value in the array represents maximum jump length at that index

return true if you can reach the last index with jumps

input: [2, 3, 1, 1, 1, 4]
                    ^

jump = i + nums[i] 
index = 1
output: true

3,2,1,0,4
        ^
jump = 3



"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        jump = 0

        for i in range(len(nums)):
            if i > jump:
                return False

            jump = max(jump, nums[i] + i)

            if jump >= len(nums) - 1:
                return True
            
        