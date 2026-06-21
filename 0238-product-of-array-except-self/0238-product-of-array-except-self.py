"""

to get the product of each array except itself in i you have to get the postfrix and prefix

start of by getting the prefix 

if we are starting at beginning the prefix will just be 1 since we cant multiply by 0

1 1 2 6
this would be prefix

create a prefix array just intialize it to all 1

then start at index 1 and multiply it by 1 and make the new prefix be prefix * nums[i -1]


1,2,3,4
  ^
1 12 8 6
^

postfix = 12

"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1

        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            result[i] = prefix

        postfix = 1

        for i in range(len(nums) -2, -1, -1):
            postfix *= nums[i + 1]
            result[i] *= postfix

        return result

