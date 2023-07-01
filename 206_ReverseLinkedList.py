# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we create a current value to keep track of the head and a previous value so the head can point to an empty node when initially reversing
        current, previous = head,None

        # while we havent reached the end of our linked list
        while current != None:
            # get the head.next value before we change it to point to behind
            current = head.next
            # set our head to point to behind itself to reverse the list
            head.next = previous
            # we then move up our previous value so that it points to our original head
            previous = head
            # we then move our head forward with the saved current value we got at the beginning
            head = current

        # we have to return previous because returning current would point to empty space
        return previous