from ds import TreeNode
from typing import Optional, List
from utils import build_tree_from_list, visualize_tree, visualize_tree_from_array

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca: TreeNode = None

        def dfs(node: TreeNode) -> TreeNode:
            nonlocal lca

            if not node:
                return None
            
            isNode: bool = node == p or node == q

            left: TreeNode = dfs(node.left)
            right: TreeNode = dfs(node.right)

            if (isNode and (left or right)) or \
               (left and right):
                lca = node
                return lca
            
            if isNode:
                return node

            return left if left else right
        
        dfs(root)
        return lca
    
s = Solution()
tree1 = build_tree_from_list([5,3,8,1,4,7,9,None,2])
p: TreeNode = tree1.left.left.right # 2
q: TreeNode = tree1.left.right # 4
tree2 = build_tree_from_list([1])
visualize_tree(tree1)
print("--------------")
visualize_tree(p)
print("--------------")
visualize_tree(q)
print("--------------")
visualize_tree(s.lowestCommonAncestor(tree1, p, q))