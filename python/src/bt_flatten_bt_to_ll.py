from typing import Optional, List
from ds import TreeNode
from utils import build_tree_from_list, visualize_tree

class Solution:
    def flatten1(self, root: Optional[TreeNode]) -> None:
        head: TreeNode = TreeNode(-1, None, None)

        def dfs(node: TreeNode, head: TreeNode):
            if not node:
                return head
            
            head.right = TreeNode(node.val, None, None)
            new_head = head.right
            if node.left:
                new_head = dfs(node.left, new_head)
            if node.right:
                new_head = dfs(node.right, new_head)
        
            return new_head

        dfs(root, head)
        return head.right
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node: TreeNode) -> TreeNode:           
            left = node.left
            right = node.right
            next = node
            
            if left:
                next.right = left
                next.left = None
                next = dfs(left)
            
            if right:
                next.right = right
                next.left = None
                next = dfs(right)
            
            return next

        dfs(root)
        

s = Solution()

arrs = [[1,2,5,3,4,None,6]]
for arr in arrs:
    tree = build_tree_from_list(arr)
    visualize_tree(tree)
    s.flatten(tree)
    visualize_tree(tree)