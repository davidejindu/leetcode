class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0

        wordList.append(beginWord)

        wordMap = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                wordMap[pattern].append(word)


        queue = deque([beginWord])
        visited = set([beginWord])
        result = 1


        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neighbor in wordMap[pattern]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)

            result +=1

        return 0
