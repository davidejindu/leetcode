class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """"
        AABABBA         k = 1
        l
        r

         A:2, B:1 
         length = 3
          3 - 2 =< k
         max = 3

        keep getting the max values in hashmap
        if the max value in hashmap 
        get r - l + 1 - max_value in hashmap > l +=1 else get max lenght


    """

        window_map = {}
        l = max_freq = max_replacement = 0

        for r in range(len(s)):
            window_map[s[r]] = 1 + window_map.get(s[r], 0)
            max_freq = max(window_map.values())
            if (r - l + 1) - max_freq <= k:
                max_replacement = max(max_replacement, r - l + 1)
            else:
                window_map[s[l]] -=1
                l +=1

        return max_replacement