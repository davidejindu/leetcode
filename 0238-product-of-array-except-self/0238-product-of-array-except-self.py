class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """"
        must find the prefix and postfix of nums[i]
        so create a prefix array itll be the same length but all 1

        [1,1,8,6]
             i

        [1,2,3,4]
               i
        start traversing at index 1 
        nums[i] nums[i] * nums[i -1]



        """

        prefix_list = [1] * len(nums)
        prefix = 1
        for i in range(1, len(nums)):
            prefix *= nums[i - 1] 
            prefix_list[i] *= prefix


        postfix = 1 

        for i in range(len(nums) -2, -1, -1):
            postfix *= nums[i + 1]
            prefix_list[i] *= postfix

        return prefix_list