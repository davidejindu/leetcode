class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        s = "ADOBECODEBANC", t = "ABC"
             l
             r

        countT = {A:1, B:1, C:1}
        countS = {A: 1, B:2, C:1}
        have = 3
        need = 2
        shouldn't have be sum not len?
        if its len then it wont account for multiple key values



        """

        l = 0
        result = [-1,-1]
        minimum_substring = float('inf')
        countT = defaultdict(int)
        countS = defaultdict(int)

        for char in t:
            countT[char] +=1

        need, have = len(countT), 0




        for r in range(len(s)):
            countS[s[r]] +=1
            
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have +=1

            while have == need:
                if r - l + 1 < minimum_substring:
                    minimum_substring = r - l + 1
                    result = [l,r]

                countS[s[l]] -=1

                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -=1
                l +=1

        if minimum_substring == float('inf'):
            return ""
        else:
            l, r = result
            return s[l:r +1]