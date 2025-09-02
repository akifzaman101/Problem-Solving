# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    
# Example usage:
solution = Solution()
print(solution.deleteDuplicates([1,1,2]))  # Output: [1,2]
print(solution.deleteDuplicates([1,1,2,3,3]))  # Output: [1,2,3]