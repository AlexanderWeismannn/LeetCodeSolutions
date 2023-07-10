# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using floyds totoise and hare algorithm
        slow,fast = head,head

        # while we havent reached the end of a list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # this can be done because we are comparing the places in memory
            # of the linked list nodes so even if they have the same val
            # they will be different
            if slow == fast:
                return True



        return False
        

