class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """

        s = "ADOBECODEBANC", t = "ABC"  output = "BANC"
                       l
                         r
             A:1, B:1, C:1
             have = 3
             need = 3
             min_substring = "BANC" 4  

        """
        if s == t:
            return s

        map_t = {}
        
        for char in t:
            map_t[char] = 1 +map_t.get(char,0)

        have,need = 0, len(map_t)
        map_s = {}
        min_substring = ""
        l = 0

        for r in range(len(s)):
            if s[r] in map_t:
                map_s[s[r]] = 1 + map_s.get(s[r],0)
            
            if s[r] in map_t and map_s[s[r]] == map_t[s[r]]:
                have +=1
    
            while have == need:
                if not len(min_substring):
                    min_substring = s[l:r+1]
                elif min_substring and r - l + 1 < len(min_substring):
                    min_substring = s[l:r + 1]

                if s[l] in map_s:
                    map_s[s[l]] -=1
                    if map_s[s[l]] < map_t[s[l]]:
                        have -=1
                l +=1 

        return min_substring



