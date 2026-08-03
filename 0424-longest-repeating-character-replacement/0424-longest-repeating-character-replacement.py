"""

your given a string s and integer k choose any char of string and replace it with any upperchase english cahracter i can perform it at most k times

return the length of longest substring containing same letter after making k changes
so i want to take the max character and subtract it by the window and if its less than or equal
to k i can replace it by the substring to get the largest have a hashmap

input: "ABAB" k = 2

output = 4

A A B A B B A
  l
          r

char_map {A:2, B:3}
result = 5
maxx = 3
k = 2
window_len = 5






"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        char_map = defaultdict(int)
        maxx = 0
        result = 0

        for r in range(len(s)):
            window_len = r - l + 1
            char_map[s[r]] +=1
            maxx = max(char_map.values())
            if window_len - maxx <= k:
                result = window_len

            else:
                char_map[s[l]] -=1
                l +=1

        return result

        