class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class Queue():
    def __init__(self) -> None:
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def peak(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

class BinaryTree():
    def __init__(self,value) -> None:
        self.root = Node(value)

    def preorder(self, start, traversal):
        # Root -> Left -> Right
        if start is None:
            return
        
        traversal.append(start.value)
        self.preorder(start.left, traversal)
        self.preorder(start.right, traversal)
        return traversal
    
    def inorder(self,start, traversal):
        # Left -> Root -> Right
        if start is None:
            return
        
        self.inorder(start.left, traversal)
        traversal.append(start.value)
        self.inorder(start.right, traversal)
        return traversal

    def postorder(self,start, traversal):
        # Left -> Right -> Root
        if start is None:
            return

        self.postorder(start.left, traversal)
        self.postorder(start.right, traversal)
        traversal.append(start.value)
        return traversal
    
    def level_order(self, start):
        # Level Order Traversal
        if start is None:
            return []
        
        queue = Queue()
        traversal = []
        queue.enqueue(start)
        
        while len(queue.items) > 0:
            node = queue.dequeue()
            if node is not None:
                traversal.append(node.value)
                if node.left is not None:
                    queue.enqueue(node.left)
                if node.right is not None:
                    queue.enqueue(node.right)
        return traversal

tree = BinaryTree(3)

# Adding a left child to the root node
tree.root.left = Node(4)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right = Node(5)
tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

print(tree.preorder(tree.root,[]))  # Output: [3, 4, 6, 7, 5, 8, 9]
print(tree.inorder(tree.root,[]))  # Output: [6, 4, 7, 3, 8, 5, 9]
print(tree.postorder(tree.root,[]))  # Output: [6, 7, 4, 8, 9, 5, 3]
print(tree.level_order(tree.root))  # Output: [3, 4, 5, 6, 7, 8, 9]