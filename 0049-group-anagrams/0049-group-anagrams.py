class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        loop through each character in word 
        get the ascii and increment
        make hashmap the ascii with numbers and the values the word




        """
        anagram_map = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] +=1

            anagram_map[tuple(count)].append(word)

        return list(anagram_map.values())
     
        