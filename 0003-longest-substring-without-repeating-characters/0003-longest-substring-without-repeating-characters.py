class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
       "abcabcbb"
        ^
           ^
        max_window = 3
        both pointers start at 0 
        if s[r] not in hashSet increase the maxwindow

        if its in hashset dont add then get max subset
        after that remove s[l] from result
        increment l+=1

        """

        max_window = 0
        unique = set()
        l, r = 0,0

        """
       "abcabcbb"
        ^
           ^
         3
        unique {a,bc}
           """
        while r < len(s):
            
            
            #increase substring without duplicate
            while r < len(s) and s[r] not in unique:
                unique.add(s[r])
                r +=1

            max_window = max(max_window, r - l)
            print(l,r,max_window)

            #remove duplicate

            while r < len(s) and s[r] in unique:
                unique.remove(s[l])
                l +=1 

        return max_window