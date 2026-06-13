class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        result = max(nums)

        maxx, minn = 1,1 

        for n in nums:
            if n == 0:
                maxx = minn = 1

            tmp = maxx * n
            maxx = max(maxx * n, minn * n, n)
            minn = min(tmp, minn * n, n)

            result = max(result, maxx)

        return result

            
        