class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = l = 0
        substring_set = set()

        for r in range(len(s)):
            while s[r] in substring_set:
                substring_set.remove(s[l])
                l +=1

            substring_set.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length

                
       

            