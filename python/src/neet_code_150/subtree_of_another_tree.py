from ds import TreeNode
from typing import Optional, List
from utils import build_tree_from_list, visualize_tree, visualize_tree_from_array

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        nodes: List[TreeNode] = []

        if not subRoot or not root:
            return False
        
        # 1. Search subRoot node in root
        def find_nodes(root: TreeNode, node: TreeNode):
            nonlocal nodes
            if not root:
                return
            
            if node.val == root.val:
                nodes.append(root)

            find_nodes(root.left, node)
            find_nodes(root.right, node)

            return

        # 2. If it exists compare the trees from that node downward
        def are_the_same_tree(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            
            return (node1.val == node2.val) and \
                are_the_same_tree(node1.left, node2.left) and \
                are_the_same_tree(node1.right, node2.right)
        
        result: bool = False
        find_nodes(root, subRoot)
        for node in nodes:
            result |= are_the_same_tree(node, subRoot)
            if result:
                return result
        return False

s = Solution()
tree1 = build_tree_from_list([1,1])
tree2 = build_tree_from_list([1])
visualize_tree(tree1)
visualize_tree(tree2)
print(s.isSubtree(tree1, tree2))