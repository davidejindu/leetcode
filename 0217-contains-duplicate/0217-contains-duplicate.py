class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup_map = set()

        for number in nums:
            if number in dup_map:
                return True

            dup_map.add(number)
        
        return False