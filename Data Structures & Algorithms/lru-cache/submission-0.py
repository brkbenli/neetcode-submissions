class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # maps key to nodes
        self.left = Node(0, None)
        self.right = Node(0, None)

        # left finds lru right is mru
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            returnVal = self.cache[key].val
            # used the val so move to most recent used
            returnNode = self.cache[key]
            # remove node link
            if returnNode.prev:
                prevNode = returnNode.prev
                prevNode.next = returnNode.next
                returnNode.next.prev = prevNode
                # move node to end of list
                endofLL = self.right
                previousOfEnd = endofLL.prev
                previousOfEnd.next = returnNode
                returnNode.next = endofLL
                returnNode.prev = previousOfEnd
                self.right.prev = returnNode
                return returnNode.val  
        return -1
        

    def put(self, key: int, value: int) -> None:

        # updates value
        if key in self.cache:
            self.cache[key].val = value
        else:
            self.cache[key] = Node(key, value)
            self.cap -= 1

        # if cap is full
        if self.cap < 0:
            removeNode = self.left.next
            nextNode = removeNode.next
            self.left.next = nextNode
            nextNode.prev = self.left
            self.cache.pop(removeNode.key)
            self.cap += 1
        # remove node link
        returnNode = self.cache[key]
        if returnNode.prev:
            prevNode = returnNode.prev
            prevNode.next = returnNode.next
            returnNode.next.prev = prevNode
        # move node to end of list
        endofLL = self.right
        previousOfEnd = endofLL.prev
        previousOfEnd.next = returnNode
        returnNode.next = endofLL
        returnNode.prev = previousOfEnd
        self.right.prev = returnNode
            
        
        
        

        
        
