from ds import TreeNode
from typing import Optional, List, Deque
from utils import build_tree_from_list, visualize_tree, visualize_tree_from_array

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result: int = 0

        def dfs(node: TreeNode, path_max:int):
            nonlocal result
            if not node:
                return
            
            if node.val >= path_max:
                print(f"{path_max} < {node.val}")
                result += 1
                path_max = node.val
            
            dfs(node.left, path_max)
            dfs(node.right, path_max)
            

        dfs(root, -1000)
        return result    

s = Solution()
trees = [
    build_tree_from_list([3,1,4,3,None,1,5]),
    build_tree_from_list([2,1,1,3,None,1,5]),
    build_tree_from_list([1,2,-1,3,4]),
    build_tree_from_list([1,2,3,4,5,6,7]),
    build_tree_from_list([1]),
    build_tree_from_list([]),
]
for tree in trees:
    visualize_tree(tree)
    print(s.goodNodes(tree))