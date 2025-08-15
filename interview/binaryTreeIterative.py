from typing import List

class TreeNode:
    def __init__(self, value,left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        memory = {}
        
        for i,e in enumerate(inorder):
            memory[e] = i

        # Build the tree
        root = self.helper(preorder[::-1], inorder, 0, len(inorder), memory)

        return root

    def helper(self, preorder, inorder, leftPointer, rightPointer, memory):
        if leftPointer >= rightPointer:
            return None

        num = preorder.pop()
        root = TreeNode(num)
        idx = memory.get(num)
        
        root.left = self.helper(preorder, inorder, leftPointer, idx, memory) if idx > leftPointer else None
        root.right = self.helper(preorder, inorder, idx + 1, rightPointer, memory) if idx < rightPointer else None

        return root

# Example usage
if __name__ == "__main__":
    bt = BinaryTree()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = bt.buildTree(preorder, inorder)
    print("Root:", root.value)
    print("Left Child of Root:", root.left.value if root.left else None)
    print("Right Child of Root:", root.right.value if root.right else None)
    print("Left Grandchild of Root:", root.left.left.value if root.left and root.left.left else None)
    print("Right Grandchild of Root:", root.right.right.value if root.right and root.right.right else None)