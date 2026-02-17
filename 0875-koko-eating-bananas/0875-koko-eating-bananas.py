class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        """

        len(piles) = n
        k is bananas per hour speed
        each hour she chooses some pile of bananas and eats k bananas 
        h = hours 
        if pile has less than k koko still stays on that pile for an hour
        whats the minimum k where she can eat all bananas within h

        so if h = 5 and n = 5 it has to be the max of piles because can't afford to     spend more than one hour on a single pile



        """

        def valid_bananas_per_hour(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile/k)

            return hours <= h
            


        l,r = 1, max(piles)

        while l < r:
            k = (l+r)//2

            if valid_bananas_per_hour(k):
                r = k

            else:
                l = k + 1

        return r

        


