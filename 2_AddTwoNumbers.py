# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        current = new_head
        carry = 0

        #progress though each Node
        while l1 or l2:
            
            # if the node exists add the value else default it 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # sum up the values and add the carry if needed
            sum_list = v1 + v2 + carry

            #get the new carry and remainder values
            carry = sum_list//10 # value to carry over
            rem = sum_list % 10 # value to add onto the current pos

            #create a new node and add the remainder value to it
            current.next = ListNode(rem)


            #update all the pointers
            current = current.next
            l1 = l1.next if l1 else None # if we dont have another node in the list default it to None
            l2 = l2.next if l2 else None # if we dont have another node in the list default it to None
            

        #check if we have and carry left over to add it 
        if carry > 0:
            current.next = ListNode(carry)
            
        # we return head.next since the original head value is a dummy pointer at the beginning of the list
        return new_head.next


