class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for number in nums:
            result = result ^ number

        return result