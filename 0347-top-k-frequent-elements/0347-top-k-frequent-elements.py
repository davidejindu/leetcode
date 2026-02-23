class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """

        the most unique elements it can be is len of nums
        since they can appear multiple times create a list where each 
        element contains a list and append to that element
        use a hashmap to keep count of how much that element appears
        if it appears 5 times make it index 5 of the list 
        then traverse through the list and keep append values until the result == k

        """

        frequency_list = [[] for i in range(len(nums) + 1)]


        count_map = {}

        for num in nums:
            count_map[num] = count_map.get(num,0) +1


        for num, count in count_map.items():
            frequency_list[count].append(num)

        print(frequency_list)

        result = []
        for list_index in range(len(frequency_list) - 1, -1, -1):
            for val in frequency_list[list_index]:
                result.append(val)
                if k == len(result):
                    return result

    
        