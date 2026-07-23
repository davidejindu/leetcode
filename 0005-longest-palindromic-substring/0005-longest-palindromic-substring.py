class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def is_palindrome(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -=1
                r +=1

            return s[l+1:r]

        max_palidrome = ""

        for i in range(len(s)):
            odd = is_palindrome(i,i)
            even = is_palindrome(i,i+1)

            if len(odd) > len(even):
                maxx = odd
            else:
                maxx = even

            if len(maxx) > len(max_palidrome):
                max_palidrome = maxx

        return max_palidrome