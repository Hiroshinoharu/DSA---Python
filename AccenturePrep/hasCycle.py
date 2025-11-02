# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Intialise 2 pointers slow and fast
        slow = head
        fast = head

        # Iterate as long as the next 2 heads are not nulls
        while fast != None and fast.next != None:
            
            # We are gonna increase the slow pointer by 1 step
            slow = slow.next

            # We are gonna do the fast pointer by 2
            fast = fast.next.next

            # If the slow pointer meets the fast pointer a full cycle is completed
            if slow == fast:
                return True
        
        return False