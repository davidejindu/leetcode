class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)

        curMax = 1
        curMin = 1

        for number in nums:
            if number == 0:
                curMax = 1
                curMin = 1

            temp = curMax * number
            curMax = max(curMax * number, curMin * number, number)
            curMin = min(temp, curMin * number, number)

            result = max(result,curMax)

        return result

