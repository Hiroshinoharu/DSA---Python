from locale import currency


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        current = self.head
        
        while index != 0 and current is not None:
            current = current.next
            index -= 1
        
        return current.value if current is not None else -1
    
    def addAtHead(self, val:int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def addAtTail(self,val:int) -> None:
        new_node = ListNode(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            current = self.head
            while index-1 != 0:
                current = current.next
                index -= 1
            
            new_node = ListNode(val)
            
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
            
            self.size += 1
            
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        elif index == 0:
            if self.head is not None:
                self.head = self.head.next
                if self.head is not None:
                    self.head.prev = None
                else:
                    self.tail = None
        elif index == self.size - 1:
            if self.tail is not None:
                self.tail = self.tail.prev
                if self.tail is not None:
                    self.tail.next = None
                else:
                    self.head = None
        else:
            current = self.head
            while index != 0:
                current = current.next
                index -= 1
            
            if current.prev is not None:
                current.prev.next = current.next
            if current.next is not None:
                current.next.prev = current.prev
        
        self.size -= 1

# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.addAtHead(1)
    dll.addAtTail(2)
    dll.addAtIndex(1, 3)  # List becomes 1 -> 3 -> 2
    print(dll.get(1))  # Output: 3
    dll.deleteAtIndex(1)  # List becomes 1 -> 2
    print(dll.get(1))  # Output: 2
    dll.addAtHead(4)  # List becomes 4 -> 1 -> 2
    print(dll.get(0))  # Output: 4
    print(dll.get(2))  # Output: 2
    dll.deleteAtIndex(0)  # List becomes 1 -> 2
    print(dll.get(0))  # Output: 1
    dll.deleteAtIndex(1)  # List becomes 1