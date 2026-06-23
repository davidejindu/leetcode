"""

AABABBA    k = 1
l
    r

5 - 3
max_replacement = 2
l = 0

{A:2, B:0}

window = 1
so the only time i have to move l is if the size of window - 2 is greater than k
at that point i want to get the max size


so i need to get the longest substring of the same character
so i need a sliding window
i want to make a hashmap where the key is the letter and the value is the frequency
now i want to get the letter that appears most in that window and see if i can switch it to k then get the len



"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_map = {}
        max_replacement = 0
        l = 0

        for r in range(len(s)):
            letter_map[s[r]] = 1 + letter_map.get(s[r], 0)
            window = r - l + 1
            max_freq = max(letter_map.values())
            if k < window - max_freq:
                letter_map[s[l]] -=1
                l +=1

            max_replacement = max(max_replacement, r - l + 1)

        return max_replacement
        