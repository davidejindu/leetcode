class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        100,4,200,1,3,2

        make nums a set for O(1) lookup

        check if num -1 in set if not the keep going 
        if it is do a while loop and keep incrementing
        check that against current max return max 


        """

        """
    max_count = 0
        0
            ^
        
        """

     
        max_count = 0
        num_set = set(nums)
        for num in num_set:
            count = 0
            if num - 1 not in num_set:
                while num in num_set:
                    count += 1
                    num += 1
                max_count = max(count, max_count)





        return max_count 