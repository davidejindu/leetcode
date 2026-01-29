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
        window = {d:1,c:1, a:1 }
        3
        3
       
        """

        permutation_map = collections.defaultdict(int)
        window = collections.defaultdict(int)
        l = 0
        count = 0


        for char in s1:
            permutation_map[char] +=1

        for r in range(len(s2)):

            window[s2[r]] +=1

            
            
           # print(window, permutation_map, len(s1), r - l + 1)

            if r - l + 1 == len(s1) and not window == permutation_map:
                window[s2[l]] -=1
                if not window[s2[l]]:
                    window.pop(s2[l])
                l+=1
                count -=1

            if window == permutation_map:
                return True


        return False