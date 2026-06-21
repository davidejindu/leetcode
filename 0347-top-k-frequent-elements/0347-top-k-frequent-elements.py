"""
return the the most k freq elements 
make an array that hold where the max frequency possible

inside of each element append to the index if it matches the freq the  element appears

get that by creating a hashmap of the number with the value being its freq


after you store each number in the correct freq loop backwards until you have 
appended k elements to the result



"""



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]

        freq_map = {}

        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)

        for num, count in freq_map.items():
            freq[count].append(num)

        result = []

        for i in range(len(nums), -1, -1):
            for nums in freq[i]:
                result.append(nums)
                if len(result) == k:
                    return result

        