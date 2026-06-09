class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        max_length = 0

        def expand(l,r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -=1
                r +=1

            return s[l+1:r]

        for i in range(len(s)):

            odd = expand(i,i)
            even = expand(i, i + 1)

            if len(odd) > len(longest_palindrome):
                longest_palindrome = odd
            
            if len(even) > len(longest_palindrome):
                longest_palindrome = even

        return longest_palindrome
            


        