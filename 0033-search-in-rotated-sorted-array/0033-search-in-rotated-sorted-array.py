class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        4,5,6,7,0,1,2
        l
              m
                    r

        if mid > r then we know the left portion is sorted
        so do if target > = num l and target < r

        else 
        then the right portion is sorted
        so do if target > mid and target <= r



        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[r]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1