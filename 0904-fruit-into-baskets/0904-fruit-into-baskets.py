class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        use hashmap to hold the fruits[i] count
        when count is greater than 3 keep moving l pointer while subtracting value
        when count[l] not in hashmap pop it then keep moving to right until reach end
        store all the totals to keep largest value

        [0,1,2,2]
           l
             r
         {1:1, 2:1  }
         total = 2
        """

        l, total, max_num = 0,0,0
        count = collections.defaultdict(int)

        for r in range(len(fruits)):
            count[fruits[r]] +=1
            total +=1

            while len(count) > 2:
                fruit = fruits[l]
                count[fruit] -=1
                total -=1
                l+=1

                if not count[fruit]:
                    count.pop(fruit)


            max_num = max(total,max_num)


        return max_num


            

        