"""
aaaaaaaaaaaabbbbbcdd   abcdd
l  
                   r

t = {A:1, B:1, C:1, D:2}
s = {A:12, B:5, C:1, D:2}
min_substring = "" 
substring_len = inf
have = 4
need = 4

"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        s_map = {}
        substring_len = float('inf')
        min_substring = ""
        l = 0

        for char in t:
            t_map[char] = 1 +t_map.get(char,0)
    
        have = 0
        need = len(t_map)

        for r in range(len(s)):
            if s[r] in t_map:
                s_map[s[r]] = 1 + s_map.get(s[r], 0)
            
                if s_map[s[r]] == t_map[s[r]]:
                    have +=1
    
            while have == need:
                if r - l + 1 < substring_len:
                    min_substring = s[l:r+1]
                    substring_len = r - l + 1

                if s[l] in s_map:
                    s_map[s[l]] -=1
                    if s_map[s[l]] < t_map[s[l]]:
                        have -=1
                
                l +=1

        return min_substring


        