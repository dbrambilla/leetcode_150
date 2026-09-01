from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val: int = val
        self.neighbors: List[Node] = neighbors if neighbors is not None else []

class ListNode:
    def __init__(self, val=0, next=None):
        self.val:int = val
        self.next:ListNode = next