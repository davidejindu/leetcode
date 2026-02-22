class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        loop through each word
        loop through each character in word
        make an array where its the length of the word 
        then increment the value of the array
        make a hashmap list where the key is a list and you append the word to the key
        return a list of the values in hashmap
        """

        anagram_map = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] +=1

            anagram_map[tuple(count)].append(word)


        return list(anagram_map.values())

        