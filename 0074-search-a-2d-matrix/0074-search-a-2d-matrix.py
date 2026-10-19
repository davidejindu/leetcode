"""
want to find the target using max a log m * n

its in a 2d matrix 
we know that first integer of each row is greater than the last integer of previous row
start at middle row by doing l + r / 2
check if the target isn't in the row
if the target is less than the row first value then go up 
if the target is greater than the row last value go down
if neither is in the case then we know that the target is in that row and we can just 


[1,3,5,7]
[10,11,16,20]
[23,30,34,60]

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            row = (l + r) // 2

            if target < matrix[row][0]:
                r = row - 1
            elif target > matrix[row][len(matrix[0]) - 1]:
                l = row + 1
            else:
                left, right = 0, len(matrix[0]) - 1
                while left <= right:
                    m = (left + right) // 2
                    if matrix[row][m] == target:
                        return True
                    elif matrix[row][m] < target:
                        left = m + 1
                    else:
                        right = m - 1

                return False

        return False
                
        