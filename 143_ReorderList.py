# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #fast pointer and slow pointer for traversing the LL. fast will get to the end while slow will get to the middle
        fast_p, slow_p = head.next,head

        # this traverses the linked list until we are at the mid point for the slow_p and the end for the fast_p
        while fast_p and fast_p.next:
            fast_p = fast_p.next.next
            slow_p = slow_p.next 

        
        # we can created a reversed part of the middle to end of the linked list now
        second = slow_p.next
        #splitting the list here
        prev = slow_p.next = None

        #reversing the split list
        while second:
            temp_next = second.next
            second.next = prev
            prev = second
            second = temp_next

        # we now merge the two linked lists together
        first,second = head,prev
        while second:
            #we insert he reverse list values between the non reversed ones
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


