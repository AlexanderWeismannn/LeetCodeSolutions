
#doubly linked list architecture with [key|val] pair
class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {} # this will map our keys to the nodes

        #default these dummy nodes
        self.left = ListNode(0,0)# left.next == LRU (Least Recently Used)
        self.right = ListNode(0,0)# right.prev == MRU (Most Recently Used) 
        self.left.next, self.right.prev = self.right,self.left

    # remove the least recently used value (I.E. left.next)
    def remove(self,listnode):
        # grab the nodes on the opposite sides of the current node and set their pointers around the current node
        prev_node = listnode.prev
        next_node = listnode.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del listnode

    # insert the new most recently used node (I.E. right.prev)
    def insert(self,listnode):
        listnode.prev = self.right.prev
        listnode.next = self.right
        self.right.prev.next = listnode
        self.right.prev = listnode 

    def get(self, key: int) -> int:
        if key in self.hashmap:
            #remove from our current list and insert at the right since it is now the MRU(most recently used)
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        else:
            return -1
     
    def put(self, key: int, value: int) -> None:
        # check if a node exists already
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            
        # create a new Node
        self.hashmap[key] = ListNode(key,value)
        # insert it again as most recent
        self.insert(self.hashmap[key])

        if len(self.hashmap) > self.capacity:
            #remove our least recently used Node
            lru = self.left.next
            # deletes the listnode
            self.remove(lru)
            #deletes the hashmap key->Node connection
            del self.hashmap[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)