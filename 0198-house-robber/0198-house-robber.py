"""
    
    1 2 3 1     output = 4

    rob1, rob2, money, money + 1

    


"""




class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0


        for money in nums:
            maxx = max(money + rob1, rob2)

            rob1 = rob2
            rob2 = maxx

        return rob2

      
   