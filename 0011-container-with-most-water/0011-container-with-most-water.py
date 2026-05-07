class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        two pointers 
        get the min height between two points then multiple the difference
        store that in max variable and proceed to go to whatever one is smaller


        """

        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            min_height = min(height[l], height[r])
            curr_height = min_height * (r - l)

            max_area = max(max_area, curr_height)

            if height[l] < height[r]:
                l +=1
            else:
                r -=1

        return max_area