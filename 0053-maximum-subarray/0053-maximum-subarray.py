"""

find the subarray with the largest sum

so brute force would be looking at each subarray and getting the max thats O(n^2)

-2,1,-3,4,-1,2,1,-5,4
                    ^

total = 1
count = 6

dont start subarray until its positive keep getting max at each turn
only restart subarray if the current total is less than 0 
if its less than 0 we wont want it 

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = float('-inf')
        total = 0
        for i in range(len(nums)):
            total += nums[i]

            maxx = max(maxx, total)

            if total < 0:
                total = 0

           

        return maxx



        