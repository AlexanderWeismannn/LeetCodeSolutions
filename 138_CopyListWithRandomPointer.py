"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # we create our map for all of the linked list values,
        # We need one edge case covered where there is a NULL value
        node_dict = {None:None}
        current = head
        #first loop to put all values in the hash map
        while current:
            copy = Node(current.val)
            node_dict[current] = copy
            current = current.next

        current = head
        #second loop to connect the nodes.next and nodes.random
        while current:
            copy = node_dict[current] 
            copy.next = node_dict[current.next]
            copy.random = node_dict[current.random]
            current = current.next


        #we return our list by calling the original head value
        return node_dict[head]


            



        
