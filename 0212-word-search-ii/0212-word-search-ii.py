class Node:

    def __init__(self):
        self.end = False
        self.children = {}

    def addWord(self,word):
        cur = self

        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()

            cur = cur.children[char]

        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = Node()
        for word in words:
            self.root.addWord(word)

        ROW, COL = len(board), len(board[0])
        result, path = set(), set()


        def dfs(node,word,r,c):
            curr = node

            if (0 > r or r >= ROW or
                0 > c or c >= COL or
                board[r][c] not in node.children or
                (r,c) in path):
                return 

            path.add((r,c))
            word += board[r][c]
            curr = curr.children[board[r][c]]

            if curr.end:
                result.add(word)


            dfs(curr,word,r+1,c)
            dfs(curr,word,r-1,c)
            dfs(curr,word,r,c+1)
            dfs(curr,word,r,c-1)
            path.remove((r,c))

        for r in range(ROW):
            for c in range(COL):
                dfs(self.root,"",r,c)

        return list(result)
        