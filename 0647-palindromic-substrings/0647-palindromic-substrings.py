class Solution:
    def countSubstrings(self, s: str) -> int:
        """

        a b c
          i
          i 

        count = 3

        aaa
         i
           i
        count = 5



        """

        count = 0

        for i in range(len(s)):
            l, r = i, i

            while (0 <= l and r < len(s)) and s[r] == s[l]:
                count +=1
                l -= 1
                r +=1

            l, r = i, i + 1

            while (0 <= l and r < len(s)) and s[r] == s[l]:
                count +=1
                l -= 1
                r +=1


        return count


            