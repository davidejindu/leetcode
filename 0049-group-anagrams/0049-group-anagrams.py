"""


given an array of string group the anagrams together

input :["eat","tea","tan","ate","nat","bat"]
output: [["bat"],["nat","tan"],["ate","eat","tea"]]

loop through each word in input
then loop through each character
make an array of count 0 * 26
whenenver you see a character get the asci of that character subtract by ascii of a
that gets you between 0 to 26 and increment
make the array the key and append the word to it
that will put the same words together
return the hashmap values in an array 

hashmap for anagram 
array for count




"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            count = [0] * 26 
            for char in word:
                count[ord(char) - ord('a')] += 1

            anagram_map[tuple(count)].append(word)


        return list(anagram_map.values())
        
        