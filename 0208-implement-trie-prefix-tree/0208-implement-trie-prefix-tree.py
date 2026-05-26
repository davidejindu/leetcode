"""
create a Node class which has its children and an endofword flag

then create a root in the trie and set it equal to a empty Node

then for insert you are going to loop through each character in word
if its already a child of the cur then set set cur to that child 


"""
class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]

        curr.end = True

    """
    apple

    {a:p, p: }


    """
        

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True



        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)