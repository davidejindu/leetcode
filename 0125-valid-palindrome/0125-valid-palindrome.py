"""

return true if palindrome or not

basically two pointers one at end other at beginning
while isalnum() which means its an alphabet or number you are going to check if lower is equal

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l +=1

            while l < r and not s[r].isalnum(): 
                r -=1

            if s[l].lower() != s[r].lower():
                return False

            r -=1
            l +=1

        return True        