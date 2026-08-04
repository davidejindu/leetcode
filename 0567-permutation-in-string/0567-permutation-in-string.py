"""


okay so a permutation is when all the characters in s1 show up in substring
of characters in s2

so what you want to do is have a hashmap of s1

and you want a sliding window to see if in that window the two hashmaps are the same

s1 = "ab", s2 = "eidbaooo"

"eidbaooo"
    l
     r
s1_map = {a:1, b:1}
s2_map = {b:1, a:1}
if len of r - l + 1 = len(s1) 
check if s1_map == s2_map if not removing s[l] and shift pointer

"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = defaultdict(int)
        s2_map = defaultdict(int)

        for char in s1:
            s1_map[char] +=1

        l = 0

        for r in range(len(s2)):
            s2_map[s2[r]] +=1

            if r - l + 1 == len(s1):
                if s1_map == s2_map:
                    return True
                else:
                    s2_map[s2[l]] -=1
                    if s2_map[s2[l]] == 0:
                        s2_map.pop(s2[l])
                    l +=1


        return False
        