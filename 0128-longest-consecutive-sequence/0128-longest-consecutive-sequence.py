class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """
        create a hashset
        add each element to hashset
        if num -1 in nums in hashset 
        add 1 
        if not then reset count


        """

        max_consecutive = 0
        store_nums = set(nums)
        print(store_nums)

        for num in store_nums:
            count = 0
            if num - 1 not in store_nums:
                while num in store_nums:
                    count +=1 
                    num +=1

                max_consecutive = max(count, max_consecutive)

        return max_consecutive

        