# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        #Null length or 0 length list edge cases
        if not lists or len(lists) == 0:
            return None

        #whjile we can still merge two lists together
        while len(lists) > 1:
            mergedLists = []
            # we step by two as we are comparing two new lists every time
            # this compares lists in sets of two until weve reached the end of list of lists
            for i in range(0,len(lists),2):
                l1 = lists[i]
                # we make sure that i+1 is in bounds
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.merge_2_lists(l1,l2))

            # after we update our lists with the new merged ones 
            lists = mergedLists

        return lists[0]
        

    # almost identical code from the leetcode easy merge two linked lists problem
    def merge_2_lists(self,l1,l2):

        # create new head, set current to it so we can iterate
        head = ListNode()
        current = head

        # while we can iterate through both lists still
        while l1 and l2:
            #add the smalles val as currents next value
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            #increment current
            current = current.next


        #we have reached the end of one list
        if l1 is None:
            current.next = l2
        else:
            current.next = l1
        
        # return the new merged lists
        return head.next

        

        
