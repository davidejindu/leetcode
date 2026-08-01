"""
return k most frequest elements 

input : [1,1,1,2,2,3], k = 2
output: 1,2


so we want first to keep track of frequency so probably create hashmap
key is the number and value is the count

then we know that the max amount of frequency is the len of nums
so create a freq array that is len nums + 1 and put the freq from hashmap into index
make sure freq array each element is a list so you can appens numbers with same freq

after that you want to loop backwards of freq and append to a result array until it 
equals k

map = {1:3, 2:2, 3:1}

freq = [[], [3], [2], [1], [], [], []]
loop backwards and you will append
[1,2]



"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = [[] for i in range(len(nums) + 1)]
        freq_map = defaultdict(int)

        #create freq map
        for number in nums:
            freq_map[number] +=1

        #put freq of number in correct spot in freq list
        for num, count in freq_map.items():
            freq_list[count].append(num)

        #append to get order
        result = []


        #loop starting at end of freq list to get highest freq first and append to result
        for i in range(len(nums), -1, -1):
            for number in freq_list[i]:
                result.append(number)
                if len(result) == k:
                    return result

        