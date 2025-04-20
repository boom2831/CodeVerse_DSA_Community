from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return result


if __name__ == "__main__":
   
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

  
    sol = Solution()
    output = sol.inorderTraversal(root)

    print("Inorder Traversal:", output)  
