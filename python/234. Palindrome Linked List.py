from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        reverse = self.reverse(slow)
        
        while reverse:
            if head.val != reverse.val:
                return False
            head = head.next
            reverse = reverse.next
        return True

        
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev