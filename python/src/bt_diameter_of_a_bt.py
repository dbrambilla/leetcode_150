from ds import TreeNode
from typing import Optional
from utils import build_tree_from_list, visualize_tree

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m: int = 0

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            
            l, r = dfs(node.left), dfs(node.right)
            nonlocal m 
            m = max(m, l + r)
            return 1 + max(l ,r)
        
        # first node with both right and left
        node: TreeNode = root
        lenght: int = 0

        while node and (not node.left or not node.right):
            node = node.left if node.left else node.right
            lenght += 1

        if not node:
            return lenght - 1
        
        l_max = dfs(node.left)
        r_max = dfs(node.right)

        return max(m, l_max + r_max, lenght + l_max, lenght + r_max)
        
    
s = Solution()

arr = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
tree = build_tree_from_list(arr)
visualize_tree(tree)
print(s.diameterOfBinaryTree(tree))

arr = [2,5,None,3,None,1,4]
tree = build_tree_from_list(arr)
visualize_tree(tree)
print(s.diameterOfBinaryTree(tree))


arr = [1,2,3,4,5]
tree = build_tree_from_list(arr)
visualize_tree(tree)
print(s.diameterOfBinaryTree(tree))
        
    
arr = [1,2]
tree = build_tree_from_list(arr)
visualize_tree(tree)
print(s.diameterOfBinaryTree(tree))
        