class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 

        """
        im thinking of hashmap
        sliding window
        for each value you add and append frequency of hashmap
        if sum of hashmap values - the highest value is greater than k
        that means that the window is too diverse and even with k it 
        wont be able to get logest repeating character replacement

        BAAA
        l
            r
        count = {B:1, A:3}, result = 3 , sum = 4 , max = 2 , k = 1
        """
        count = defaultdict(int)
        result = 0
        l, r = 0,0

        for r in range(len(s)):
            count[s[r]] +=1
            if sum(count.values()) - max(count.values()) <= k:
                result = max(result, r - l + 1)
            else:
                while sum(count.values()) - max(count.values()) > k:
                    count[s[l]] -=1
                    l +=1

        return result



















