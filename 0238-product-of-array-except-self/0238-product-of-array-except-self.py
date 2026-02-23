class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        calculate the postfix
        multiple that by the prefix to get the product of array except self

        to get product of array except self
        you must get product of values before it and after it
        so prefix of [1,2,3,4] * the postfix of [1,2,3,4]

                    [1,1,2,6]
                    to get prefix start at index 1 since prefix of first element
                    is 1 
                    so would do for 1 in range(len(nums)):
                    

        [1,2,3,4]
        
        prefix
        [1,1,2,6]

        postfix
        [24,12,4,1]

        to get postfix we need to now do postfix = 1
        loop backwards
        postfix = 1
        nums: [1,2,3,4]
        prefix :[1,1,2,6]
        for i in range(len(nums) -1, -1, -1)
        prefix[i] *= postfix
        postfix *= nums[i]


        """
    
        prefix = [1] * len(nums)
        prefix_val = 1
        for i in range(1,len(nums)):
            prefix_val *= nums[i-1]
            prefix[i] *= prefix_val
        print(prefix)

        postfix = 1

        for i in range(len(nums) -1, -1, -1):
            prefix[i] *= postfix
            postfix *= nums[i]

        return prefix



      
