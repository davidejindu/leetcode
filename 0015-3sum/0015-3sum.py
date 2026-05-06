class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        -1,0,1,2,-1,-4
        doing two pointers and since we dont want duplicates sort so we can skip over same values

        0,0,0
         i
                l
                    r

        value = -1 
        first-value = [-1,-1,2], 



        """

        result = []
        nums.sort()

        for i in range(len(nums)):
            l, r  = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i -1]:
                continue

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    l +=1

                    while l < r and nums[l] == nums[l - 1]:
                        l +=1
                    

                if nums[i] + nums[l] + nums[r] < 0 :
                    l +=1
                else: r -=1

              
            

        return result
            