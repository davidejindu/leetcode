"""
okay so create a function where you pass in a number and then you go through
each number and divide by the passed in number and if it is greater than h break
if it returns a number then its good 

so we sill do a loop up to the max number in piles because thats the most it can be





"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_val = max(piles)

        def min_k(num):
            val = 0
            for i in range(len(piles)):
                val += ceil(piles[i]/num)
                
                if val > h:
                    return False

            return True

        l, r = 1, max_val
        while l <= r:
            mid = (l + r) // 2
            if min_k(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l

            

        
        