from typing import List

class TreeNode:
    def __init__(self, value,left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # Base Case
        if len(inorder) == 0:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0]) if preorder else None

        ind = inorder.index(preorder.pop(0))  # Remove the first element from preorder
        node = TreeNode(inorder[ind])  # Create a new node with the value from inorder
        
        node.left = self.buildTree(preorder, inorder[:ind]) # Build Left subtree
        node.right = self.buildTree(preorder, inorder[ind+1:]) # Build Right subtree
        return node