"""

check if nums[i] - 1 is in the list and if not 
then loop and increment until the incremented number is not in nums
keep track of max
also turn list into nums since we are doing O(n) checks which is O(1) when in set

input = [100, 4, 200, 1, 3, 2]
     
output = 4

maxx = 1
count = 1

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxx = 0
        num_set = set(nums)

        for value in num_set:
            count = 0
            if value - 1 not in num_set:
                while value in num_set:
                    count +=1
                    value +=1

            maxx = max(count, maxx)

        return maxx


        