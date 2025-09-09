class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        result = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for value, occurance in count.items():
            freq[occurance].append(value)

        for i in range(len(freq) -1, -1, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        