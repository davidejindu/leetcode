class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack()
                    path.pop()

        backtrack()
        return result