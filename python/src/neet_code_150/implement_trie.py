from typing import Dict

class TreeNode:
    children: Dict
    is_final: bool
    
    def __init__(self):
        self.childern = dict()
        self.is_final = False

class PrefixTree:
    def __init__(self):
        self.node = TreeNode()

    def insert(self, word: str) -> None:
        curr: TreeNode = self.node
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        curr.is_final = True

    def search(self, word: str) -> bool:
        curr: TreeNode = self.node
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.is_final

    def startsWith(self, prefix: str) -> bool:
        curr: TreeNode = self.node
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True

prefixTree = PrefixTree()
print(prefixTree.startsWith("a"))
print("-----------------------")
prefixTree = PrefixTree()
prefixTree.insert("dog")
print(prefixTree.search("dog"))
print(prefixTree.search("do"))
print(prefixTree.startsWith("do"))
prefixTree.insert("do")
print(prefixTree.search("do"))