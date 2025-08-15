class Node():
    
    def __init__(self,value) -> None:
        self.value = value
        self.adjecent_list = []
        self.visted = False

class Graph():
    
    def BFS(self, node):
        
        queue = []
        queue.append(node)
        node.visted = True
        
        traversal = []
        
        while queue:
            actualNode = queue.pop(0)
            traversal.append(actualNode.value)
            
            for element in actualNode.adjecent_list:
                if not element.visted:
                    queue.append(element)
                    element.visted = True
        
        return traversal
    
    def DFS(self,node,traversal):
        node.visted = True
        traversal.append(node.value)
        
        for element in node.adjecent_list:
            if not element.visted:
                self.DFS(element, traversal)
                element.visted = False
        return traversal

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")

node1.adjecent_list.append(node2)
node1.adjecent_list.append(node3)
node1.adjecent_list.append(node4)

node2.adjecent_list.append(node5)
node3.adjecent_list.append(node6)

node4.adjecent_list.append(node7)

node3.adjecent_list.append(node1)

graph = Graph()
# print("Breadth First Search",graph.BFS(node1))  # Output: ['A', 'B', 'C', 'D', 'E', 'F', 'G']

print("Depth First Search",graph.DFS(node1, []))  # Output: ['A', 'B', 'E', 'C', 'F', 'D', 'G']