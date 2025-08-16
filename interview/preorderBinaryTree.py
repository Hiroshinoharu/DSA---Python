# Define the binary tree class node 
from typing import List


class TreeNode:
    def __init__(self,value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        # Create the root
        root = TreeNode(preorder[0])

        # Initialize the stack
        stack = [root]
        
        for i in range(1, len(preorder)):
            # Create a new node if the current value is less than the last value in the stack
            if preorder[i] < stack[-1].value:
                # Create a new left child for the last node 
                node = TreeNode(preorder[i])
                stack[-1].left = node
                stack.append(node)
            else:
                # Find the right parent
                while stack and preorder[i] > stack[-1].value:
                    last = stack.pop()

                # Create a new right child for the last node
                last.right = TreeNode(preorder[i])
                stack.append(last.right)
        return root


# Create the binary search tree from the preorder traversal
preorder = [8, 5, 1, 7, 10, 12]
bst = BinaryTree()
root = bst.bstFromPreorder(preorder)