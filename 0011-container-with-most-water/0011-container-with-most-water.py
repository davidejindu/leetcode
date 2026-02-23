class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        two pointers

        the maximum is basically just the min of height[r] and height[l] * r - l

        """

        l, r = 0, len(height) - 1
        max_height = 0

        while l < r:
            min_height = min(height[l], height[r])
            current_height = min_height * (r - l)

            max_height = max(max_height, current_height)

            if height[l] < height[r]:
                l +=1
            else:
                r -=1

        return max_height