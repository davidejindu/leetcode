class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0
        nums_set = set(nums)

        for number in nums_set:
            count = 0
            if number - 1 not in nums_set:
                while number in nums_set:
                    count +=1 
                    number +=1

                maxCount = max(maxCount, count)

        return maxCount