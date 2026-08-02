class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_substring = l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l +=1

            seen.add(s[r])

            max_substring = max(max_substring, r - l + 1)

        return max_substring
        