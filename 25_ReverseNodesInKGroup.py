# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        #node that points to the head 
        dummy = ListNode(0,head)
        #node right before our new group
        group_prev = dummy

        while True:
            
            kth_node = self.get_kth_node(k,group_prev)

            #if this value is null then we have gotten to the end of the list
            if not kth_node:
                break

            #start of our new group
            group_next = kth_node.next

            #reversing the group
            prev = kth_node.next # for when we eventually have reverse the entire group of the list
            curr = group_prev.next

            #basic reverse linked list alg
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # our original next vlaue is tmp
            # we then set our group_prev.next to be equal to the new next value which is k after everything has be reversed
            # we then set our new prev vale to the original (i.e.) tmp val
            tmp = group_prev.next
            group_prev.next = kth_node
            group_prev = tmp

        return dummy.next


    # helper function to return the kth position in our list per iteration
    def get_kth_node(self,k,curr):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
