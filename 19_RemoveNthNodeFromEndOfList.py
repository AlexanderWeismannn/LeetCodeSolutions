# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we create a dummy node value to place at the start of the linked list
        # this will allow us othave our left pointer be 1 before our n from the right value
        # letting us skip that node
        dummy_node = ListNode(0,head)

        left = dummy_node
        right = head

        # we create the offset for the right node
        for i in range(n):
            right = right.next

        # while we havent reached the end
        while right:
            #update each pointers position
            left = left.next
            right = right.next

        # we have reached the end with the right pointer and our left pointer is 1
        # before the nth node. So simply skip over it
        left.next = left.next.next

        # we return the dummy_node.next to skip the dummy value we created 
        return dummy_node.next

