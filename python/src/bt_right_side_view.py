from typing import Optional, List
from ds import TreeNode
from utils import build_tree_from_list, visualize_tree_from_array, visualize_tree
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque ([root])
        result: List[int] = []
        while queue:
            level_size = len(queue)
            while level_size > 0:
                node: TreeNode = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_size -= 1
                if level_size == 0:
                    result.append(node.val)

        return result

s = Solution()

tree = build_tree_from_list(arr = [1,2,3,None,5,None,4])
visualize_tree_from_array(arr = [1,2,3,None,5,None,4])
visualize_tree(tree)
print(s.rightSideView(tree))

tree = build_tree_from_list(arr = [1,2,3,4,None,None,None,5])
visualize_tree_from_array(arr = [1,2,3,4,None,None,None,5])
visualize_tree(tree)
print(s.rightSideView(tree))