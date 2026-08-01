"""

given an integer array nums, return all the triples such that their is no duplicates among the indexes

input = -1,0,1,2,-1,-4

output = [[-1,-1,2],[-1,0,1]]

want to sort the array so that you can have a two sum approach

0 0 0 0    val = 0
i
  j        
       k

result = [[-1,-1,2], [-1,0,1]]
if i -1 and i == i - 1 continue so no duplicates

make sure j is i + 1
do a while j < k 

if nums[i] + nums[j] + nums[k] == 0 then append to result
elif value less than 0 increment j
else decrement k
also check to make sure nums[j] != nums[j+1] increment until its different

"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0  and nums[i-1] == nums[i]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                value = nums[i] + nums[j] + nums[k]

                if value < 0:
                    j +=1
                elif value > 0:
                    k -=1

                else:
                    result.append([nums[i],nums[j], nums[k]])
                    j +=1

                    while j < k and nums[j-1] == nums[j]:
                        j +=1


        return result

            
        