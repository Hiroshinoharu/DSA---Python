class ListNode:
    def __init__(self,value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # Initialize pointers
        pre = None
        cur = head
        suc = None

        # While there are nodes to reverse
        while cur:
            # Store the next node in suc
            suc = cur.next
            # Reverse the current node's pointer
            cur.next = pre
            # Move all pointers one step forward
            pre = cur
            # Then the current pointer moves to the next node
            cur = suc
        
        return pre