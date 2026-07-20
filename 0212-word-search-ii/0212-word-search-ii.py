class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self,word):
        curr = self

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]

        curr.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        result, visited = set(), set()
        root = TrieNode()

        for word in words:
            root.addWord(word)


        def dfs(r,c,node,word):
            if (0 > r or r >= ROWS or
                0 > c or c >= COLS or
                board[r][c] not in node.children or
                (r,c) in visited):
                return

            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.endOfWord:
                result.add(word)

            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)


            visited.remove((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")

        return list(result)
        