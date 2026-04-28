class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        3,2,0,0
        2,3,0,0

        4,3,3,0,0

        3,3,1,0,0


        """
        if len(nums) == 1:
            return nums[0]
            
        def rob_dp(arr):
            arr = arr.copy()
            arr.append(0)
            arr.append(0)

            for i in range(len(arr) -3, -1, -1):
                arr[i] = max(arr[i] + arr[i + 2], arr[i+1])

            return arr[0]


        return max(rob_dp(nums[:-1]), rob_dp(nums[1:]))

            