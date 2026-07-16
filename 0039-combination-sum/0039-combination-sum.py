"""
create a list of all unique combinations that sum to the target

same number can be chosen from the canidates an unlimited amount of time

backtracking

if the current sum is greater than the target return 

else keep appending that number

if value greater than target return

if i == len(candidates) return 

if value is equal to target then append to result array
also want to pop and remove the last value probably

candidates = [2,3,6,7]
subset = [2,2]
result = []     target = 7


backtrack(0,6)
backtrack(0,4)
backtrack(0,2)
backtrack(0,0)
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result, subset = [], []

        def backtrack(i, value):
            if i == len(candidates):
                return

            if value > target:
                return 

            if value == target:
                result.append(subset.copy())
                return

            subset.append(candidates[i])
            backtrack(i, value + candidates[i])

            subset.pop()
            backtrack(i + 1, value)

            
        backtrack(0,0)

        return result


        