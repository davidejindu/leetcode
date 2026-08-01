"""
return an array where the index is equal to the product of all the elements of nums except itself

to get the product of all the elements of nums except itself you need to prefix and postfix

to get prefix of first index default it to 1

input: [1,2,3,4]
output: [24,12,8,6]

prefix = [1,1,2,6]

to get prefix first set the array to all 1s 
since we know first index has to be one

nums = 1 2 3 4
           i

pre =  1 1 2 6
             i

prefix = 6
have a prefix variable that starts off as 1 and multiple nums[i - 1] to that prefix and 
set prefix[i] = prefix


now same thing but postfix
postfix variable starts off as 1

we are going to multiple the prefix array

nums    = 1 2 3 4
                i
postfix = 1 1 2 6
              i
postfix = 24



"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        prefix_arr = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            prefix_arr[i] = prefix


        postfix = 1

        for i in range(len(nums) - 2, -1, -1):
            postfix *= nums[i + 1]
            prefix_arr[i] *= postfix

        return prefix_arr
        