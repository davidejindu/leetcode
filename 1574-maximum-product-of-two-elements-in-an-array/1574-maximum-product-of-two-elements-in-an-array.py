class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        newNums = sorted(nums)

        print(newNums)

        return (newNums[len(nums)-1] -1) * (newNums[len(nums)-2] -1)