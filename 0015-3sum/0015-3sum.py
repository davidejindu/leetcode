"""
-1,0,1,2,-1,-4

-4,-1,-1,0,1,2
    i
         l
           r
0
[-1,-1,2]

two pointers but set one pointer at the beginning

make sure the first pointer is never the same as the previous that might cause duplicates

when doing two pointers after getting a val that is 0 append it but then you 
after getting target check if the l -1 == l if so you have to move l pointer again or duplicate
everytime you get the target increment

also if l is < 0 increment if it is greater decrement the r
"""




class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            #never want to start off with same first value to prevent duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                val = nums[i] + nums[l] + nums[r]

                if val == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    l +=1
                    while l < r and nums[l] == nums[l - 1]:
                        l +=1

                elif val < 0:
                    l +=1
                else:
                    r -=1

            

        return result


        