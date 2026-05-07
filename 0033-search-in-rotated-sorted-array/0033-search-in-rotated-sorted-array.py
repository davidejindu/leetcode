class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        4,5,6,7,0,1,2   target = 0
                l
                  m
                r

        so if mid is greater than r we know that the left right portion is sorted
        increasing order 
        so if target is less than r  its in that range
        thus l = mid + 1
        now if target is greater than r then set r = m because its in that range
        
        """


        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[r]:
                if nums[l] <= target and target < nums[mid] :
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1



        return -1
