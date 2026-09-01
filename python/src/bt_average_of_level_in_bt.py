from ds import TreeNode
from typing import Optional, List
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        queue = deque ([root])
        result: List[int] = [root.val]
        while queue:
            level_size = len(queue)
            values_sum = 0
            count = 0
            while level_size > 0:
                node: TreeNode = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    values_sum += node.left.val
                    count += 1
                if node.right:
                    queue.append(node.right)
                    values_sum += node.right.val
                    count += 1
                level_size -= 1

            if count > 0:
                result.append(values_sum / count)

        return result