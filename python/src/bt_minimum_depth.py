from typing import Optional
from collections import deque
from ds import TreeNode
from utils import build_tree_from_list

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])        
        level = 1
        while queue:
            level_size: int = len(queue)          
            while level_size > 0:
                node: TreeNode = queue.popleft()
                # Track the first leaf we encounter
                if not node.left and not node.right:
                    return level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_size -= 1
            level += 1
            
        return -1

s = Solution()    
tree = build_tree_from_list(arr = [3,9,20,None,None,15,7])
print(s.minDepth(tree))

tree = build_tree_from_list(arr = [2,None,3,None,4,None,5,None,6])
print(s.minDepth(tree))

tree = build_tree_from_list(arr = [2])
print(s.minDepth(tree))

tree = build_tree_from_list(arr = [1,2,3])
print(s.minDepth(tree))

tree = build_tree_from_list(arr = [])
print(s.minDepth(tree))