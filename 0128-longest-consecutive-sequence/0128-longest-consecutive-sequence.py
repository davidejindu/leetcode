class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0
        numSet = set(nums)

        for num in numSet:
            count = 0
            if num -1 not in numSet: 
                
                while num in numSet:
                    count +=1
                    num +=1

                maxCount = max(count, maxCount)

        return maxCount
                
