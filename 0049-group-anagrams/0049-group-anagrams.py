class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        group_anagram = defaultdict(list)


        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] +=1

            group_anagram[tuple(count)].append(word)


        return list(group_anagram.values())
        