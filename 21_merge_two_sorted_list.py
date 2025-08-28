from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            Head = list1
            list1 = list1.next
        else:
            Head = list2
            list2 = list2.next
            
        Final_list = Head
        
        while list1 and list2:
            if list1.val < list2.val:
                Final_list.next = list1
                list1 = list1.next
            else:
                Final_list.next = list2
                list2 = list2.next
            Final_list = Final_list.next
        
        if list1:
            Final_list.next = list1
        else:
            Final_list.next = list2
            
        return Head
    
# Example usage:
solution = Solution()
# Creating first sorted linked list: 1 -> 2 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))
# Creating second sorted linked list: 1 -> 3 -> 4
list2 = ListNode(1, ListNode(3, ListNode(4)))
merged_list = solution.mergeTwoLists(list1, list2)
# Print merged linked list
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
