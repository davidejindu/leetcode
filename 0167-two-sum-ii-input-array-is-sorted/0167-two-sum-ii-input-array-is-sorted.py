class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        """
        [3,24,50,79,88,150,345] target = 200
         l                  r


        """
        
        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left +1, right +1]

            elif numbers[left] + numbers[right] < target:

                left +=1

            else:
                right -= 1