class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]

        countFrequency = {}

        for num in nums:
            countFrequency[num] = countFrequency.get(num, 0) + 1

        for num, frequency in countFrequency.items():
            freq[frequency].append(num)

        
        result = []


        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result