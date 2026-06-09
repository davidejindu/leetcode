"""

input is a string need to return longest palindrome
all of charcters are digiest and english letters

input is a string
output is string of longest palindrome

input = babad
        brute force O(n^2) is a double for loop

        at each character in input check if its a palindrome


result = bab

        babad
          i
           j

        bab



"""



class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        max_length = -1

    
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False

                l +=1
                r -=1

            return True

        for i in range(len(s)):

            for j in range(i,len(s)):
                if isPalindrome(i,j) and j - i + 1 > max_length:
                    longest_palindrome = s[i:j + 1]
                    max_length = j - i + 1

            if len(s) - i <= max_length:
                return longest_palindrome

            



        