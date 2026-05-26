class Node:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]

        cur.end = True
        

    def search(self, word: str) -> bool:

        def dfs(j,root):
            curr = root

            for i in range(j,len(word)):
                char = word[i]

                if char == ".":
                    for val in curr.children.values():
                        if dfs(i+1,val):
                            return True
                    return False

                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]

            return curr.end

        return dfs(0,self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)