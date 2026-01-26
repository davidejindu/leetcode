class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
       

        if len(s) < len(t):
            return ""

        if len(s) == len(t) and s == t:
            return s

        countT, window = {}, {}
        l,r = 0,0
        minWindow = len(s) + 1
     
        min_substring = ""


        for char in t:
            countT[char] = countT.get(char,0) + 1

        have,need = 0, len(countT)

        while r < len(s):
            char = s[r]
            window[char] = window.get(char,0) + 1

            if char in countT and window[char] == countT[char]:
                have +=1

            r+=1
            while have == need:
                if (r - l ) < minWindow:
                    minWindow = r - l
                    min_substring = s[l:r]
            
                window[s[l]] -=1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1

                l +=1 
                print(l,r)
                

        return min_substring
        
                    

        





