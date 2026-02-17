class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        """
1,2,3,1,1 capacity = 3 days = 4

days_count = 0
count = 2
        """

        def valid_ship_capacity(capacity):
            count = 1
            days_count = 0

            for weight in weights:
                if days_count + weight > capacity:
                    count +=1
                    days_count = 0

                days_count += weight

            return count <= days 
        
        
        l, r = max(weights), sum(weights)
        
        while l < r:

            capacity = (l + r) //2

            if valid_ship_capacity(capacity):
                r = capacity

            else:
                l = capacity + 1

        return l

