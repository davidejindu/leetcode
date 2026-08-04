"""

given two strings s and t return the minimum window substring of s
so every charachter in s is in that window

so basically have a hashmap where you get the frequency of t 
then check to make sure every character in t appears in substring of s
and get the smallest substring possible

sliding window for sure

have two varaibles a have and a need
whenever the key in s matches frequency of t increment have 
when have == need you can do your check to get the smallest substring

A D O B E C O D E B A N C
l
          r  
have = 3
need = 3 (len(t hashmap))
countT = {A:1, B:1, C:1}
countS = {A:1, D:1, O:1, B:1, E: 1, C:1}

have == need
now do while have == need 
you want to get smallest substring

if not min_substring or r - l + 1 < len(min_substring):
    min_substring = s[l:r+1]

    s[l] -=1
    if s[l] in countT and countS[s[l]] < countT[s[l]]:
        have -=1

    l +=1




"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or len(s) < len(t):
            return ""

        countT = defaultdict(int)
        countS = defaultdict(int)

        for char in t:
            countT[char] +=1

        have = 0
        need = len(countT)
        l = 0
        min_substring = ""

        for r in range(len(s)):
            countS[s[r]] +=1

            if s[r] in countT:
                if countS[s[r]] == countT[s[r]]:
                    have +=1
           
            while have == need:
                if not min_substring or r - l + 1 < len(min_substring):
                    min_substring = s[l:r +1]

                countS[s[l]] -=1

                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1

                l +=1

        return min_substring

        