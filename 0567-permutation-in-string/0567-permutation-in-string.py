class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        make hashmap of s1

        loop through s2 and append to window hashmap
        if at any point window == s1 hashmap we found a permutation
        if hashmap r - l + 1 == len(s1) increment l

        s2 = dcda
             l
                r   


        s1 = adc

        permutation_map = {a:1,d:1, c:1}
        window = {d:2,c:1,a:1 }
        have = 3
        need = 3
       
        """

        s1_map = collections.defaultdict(int)
        window = collections.defaultdict(int)
        l = 0
        


        for char in s1:
            s1_map[char] +=1

        have,need = 0, len(s1_map)

        for r in range(len(s2)):

            window[s2[r]] +=1

            if s2[r] in s1_map and window[s2[r]] == s1_map[s2[r]]:
                have +=1

            if r - l + 1 > len(s1):
                left = s2[l]

                if left in s1_map and window[left] == s1_map[left]:
                    have -=1

                window[left] -=1
                if not window[left]:
                    window.pop(left)
                l+=1
            #print(have,need,s1_map,window,r - l + 1)
            if have == need:
                return True


            

            


        return False
