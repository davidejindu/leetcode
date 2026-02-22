class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """

    2,7,11,15

    so i want the indexes that add up to 9 
    i can create a hashmap of value and index
    if target - num in hashmap ik I have what i need
    so i can return [hashmap[target-num], i]


        """
        target_map = {}

        for index, value in enumerate(nums):
            num = target - value

            if num in target_map:
                return [target_map[num], index]

            target_map[value] = index

        print(target_map)
        return []