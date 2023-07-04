# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a new linked list with a head value, also create a current value that will step through our new linked list as values
        # are added
        head = ListNode()
        current = head

        # we make sure that we have not reached the end of either list
        while list1 and list2:
            # compare the values we are at, add the smallest as the next value in our linked list
            # Then move the head of whatever list we pulled from forward by 1
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # update our current pointer to the new position 
            current = current.next


        # we have reached the end of one of the lists, so append the non empty one to the end of our new list
        # since we know that all its values that remain are bigger than any in our current list
        if list1 is None:
            current.next = list2
        else:
            current.next = list1

        return head.next