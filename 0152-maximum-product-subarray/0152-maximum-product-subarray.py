"""

find subarray that has the largest prlduct and return the product
Input: 2,3,-2,4         Output: 6

we need to keep track of the max and min occurance we have
because if we get a negative value then the min will more than likely turn into the max

also if the value in the array is ever 0 we should reset max and min variables to 1

2 3 -2 4
     ^
maxx = -2
minn = -12
max_product = 6
temp = 2


"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = max(nums)

        minn = 1
        maxx = 1

        for val in nums:
            if val == 0:
                maxx = minn = 1
            temp = val * maxx

            maxx = max(val, temp, minn * val)
            minn = min(val, temp, minn * val)

            max_product = max(max_product, maxx)

        return max_product
        