"""


input = s: "leetcode" wordDict: ["leet", "code"]
                   ^
output : boolean

return true if s can be broken up into words that match wordDict

the same work can be used multiple time


so want to get the length of the word in wordDict

and go through s in the size so for example leet is size 4 
so you would check the first 4 letters in s and see if any word in wordDict matches it

then you want to check then you want to repeat that starting at the 5th letter since the 
4th letter was already a match

so this can be a dp

at each index you see if the start of the index to the end of the size of word is equal to the word

then you keep going till you reach the length of the word because that means you found a word
that matches s perfectly

so the base case would be when you read the len of word return true

store the true indexes so you dont check it multiple times


"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        #base case if you reach the last index in s return True
        memo[len(s)] = True

        """


        leetcode  wordDict = ["leet","code"]
        ^  ^

        dfs(0)
        s[0:4] == True
        dfs(4)
        s[4:8] == True
        dfs(8)
        8 in memo 
        return True

        memo[4] = True
        memo[0] = True

        return True


        
        
        """
        def dfs(i):
            if i in memo:
                return memo[i]

            for word in wordDict:
                if s[i:i+len(word)] == word:
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True

            memo[i] = False
            return False



        return dfs(0)
                



                
                    
                