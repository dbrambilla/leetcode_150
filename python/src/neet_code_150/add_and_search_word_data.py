
from typing import Dict
from collections import defaultdict
class TreeNode:
    children: Dict[str, 'TreeNode']
    is_final: bool
    
    def __init__(self):
        self.children = defaultdict(lambda: TreeNode())
        self.is_final = False

class WordDictionary:
    trie: TreeNode

    def __init__(self):
        self.trie = TreeNode()

    def addWord(self, word: str) -> None:
        curr: TreeNode = self.trie
        for c in word:
            curr = curr.children[c]
        curr.is_final = True

    def search(self, word: str) -> bool:
        def rec(word: str, index:int, curr: TreeNode) -> bool:
            if index == len(word):
                return False
            
            c: chr = word[index]
            found: bool = False
            for child, node in curr.children.items():
                if c == '.' or c == child:
                    if index + 1 == len(word):
                        return node.is_final
                    found = rec(word, index + 1, node)
                    if found:
                        return True
            return False
                
        return rec(word, 0, self.trie)

wordDictionary = WordDictionary()
wordDictionary.addWord("day")
wordDictionary.addWord("bay")
wordDictionary.addWord("may")
print(wordDictionary.search("say"))
print(wordDictionary.search("day"))
print(wordDictionary.search(".ay"))
print(wordDictionary.search("b.."))
print(wordDictionary.search("..."))