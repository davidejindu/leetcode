class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        create a hashmap for s1
        so do sliding window hashmap where you compare the len of s1
        with hashmap of s1

       """


        s1_map = defaultdict(int)
        s2_map = defaultdict(int)
        l = 0

        if len(s1) > len(s2) :
            return False

        for char in s1:
            s1_map[char] += 1

        """
         abcdeabcdx
         l
          r
        s1_map = {a:2,b:2, c:2, d:2, x:1, e:1}
        s2_map = {a:2, b:2, c:2,d:2, e:1, x:1}
  
        """

        for r in range(len(s2)):
            s2_map[s2[r]] +=1
    

            if r - l + 1 > len(s1) and not s2_map == s1_map:
                 s2_map[s2[l]] -=1
                 if s2_map[s2[l]] == 0:
                    s2_map.pop(s2[l])
                 l +=1

          

            if s2_map == s1_map:
                return True


        return False
