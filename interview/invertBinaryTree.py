class TreeNode:
    def __init__(self,value=0,left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    

class BinaryTree:
    def invertTree(self,root: TreeNode) -> TreeNode:
        # Base Case
        if root is None:
            return None
        else:
            # Swap the left and right children
            root.left, root.right = root.right, root.left
            # Recurively Invert the Tree
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root

# Example usage
if __name__ == "__main__":
    bt = BinaryTree()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    inverted = bt.invertTree(root)
    print("Inverted Root:", inverted.value)
    print("Inverted Left Child of Root:", inverted.left.value if inverted.left else None)
    print("Inverted Right Child of Root:", inverted.right.value if inverted.right else None)