class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        make a placeholder i 
        and then l = i+1 and r = len(nums) -1

        if nums[l] + nums[r] + nums[i] = 0 append to result then make sure
        the l r and i have different numbers then last time
              i      l     r
        [-4, -1, -1, 0, 1, 2]
        val = -1
        if i is greater than 0 we can return because everything is positive wont get 0
        """
        
        nums.sort()
        result = []
        """
      i   l r     
    [-2,0,1,1,2]

        """
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            elif i > 0 and nums[i] == nums[i -1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[l] + nums[r] + nums[i]

                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l +=1 
                    while l < r and nums[l] == nums[l -1]:
                        l+=1

                    r -=1
                    while l < r and nums[r] == nums[r + 1]:
                        r -=1

                elif total > 0:
                    r -=1
                else:
                    l +=1

        return result
            

       