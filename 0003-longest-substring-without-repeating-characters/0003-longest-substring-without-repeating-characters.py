class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        use a set to check if its in the window
        l,r = 0, 0
        if s[r] not in set append and increase the max
        if its inset keep popping left until its not
        
        longest_substring = 2
        in_substring = {d, v}
        dvdf
          r
         l
        """

        substring_set = set()
        longest_substring = 0
        l = 0

        for r in range(len(s)):
            if s[r] not in substring_set:
                longest_substring = max(longest_substring, r - l + 1)
                substring_set.add(s[r])
            else:
                while s[r] in substring_set:
                    substring_set.remove(s[l])
                    l +=1
                substring_set.add(s[r])
            print(substring_set)

        return longest_substring

            