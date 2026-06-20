class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for number in nums:
            if number in num_set:
                return True
            num_set.add(number)

        return False