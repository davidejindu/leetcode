class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_duplicate = set()

        for val in nums:
            if val in check_duplicate:
                return True
            check_duplicate.add(val)

        return False
        