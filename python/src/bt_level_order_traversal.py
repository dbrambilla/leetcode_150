from collections import deque
from typing import List, Optional
from ds import TreeNode
from utils import build_tree_from_list

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root or (not root.left and not root.right):
            return [[root.val]]
        
        queue = deque([root])
        result: List[List[int]] = []

        while queue:
            level: List[int] = []
            level_size = len(queue)

            while level_size > 0:
                node: TreeNode = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_size -= 1
            
            result.append(level)

        return result

tree = build_tree_from_list(arr = [3,9,20,None,None,15,7])
s = Solution()
print(s.levelOrder(tree))