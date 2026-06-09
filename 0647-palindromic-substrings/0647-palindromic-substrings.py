"""
expand technique

and increment count

"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromic_num = 0

        def expand(l,r):
            count = 0
            while 0 <= l and r < len(s) and s[l] == s[r]:
                count +=1
                l -=1
                r +=1

            return count


        for i in range(len(s)):
            palindromic_num += expand(i,i)
            palindromic_num += expand(i, i +1)

        return palindromic_num









        return palindromic_num