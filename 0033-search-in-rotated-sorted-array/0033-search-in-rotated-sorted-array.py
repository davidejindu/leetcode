class Solution:
    def search(self, nums: List[int], target: int) -> int:

        """
        target = 5
        5,1,3
        l 
            
        r

        target = 2
        4,5,6,7,0,1,2
        l        
                m      
                     r

        if m > r that means left is sorted

        and if target is less than m its in left side else in
        right side


        """

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r)//2
            print(nums[mid])

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[r]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1

                else:
                    l = mid + 1

            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1 

        return -1 


