class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countT, countS = {}, {}

        for char in s:
            countS[char] = 1 + countS.get(char,0)

        for char in t:
            countT[char] = 1 + countT.get(char,0)

        return countT == countS

        