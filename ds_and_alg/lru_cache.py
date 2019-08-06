class Node(object): 
    def __init__(self, key, val): 
        self.val = val
        self.prev = None
        self.next = None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.oldest = None
        self.newest = None        

    def get(self, key: int) -> int:
        
        if key not in self.map: 
            return -1
        if self.newest.key == key: 
            return self.map[key].val
        tmp = self.map[key]
        print('tmp: ', tmp.key, 'next: ', tmp.next.val if tmp.next else None, 'prev: ', tmp.prev.val if tmp.prev else None)
        prev_node = tmp.prev
        next_node = tmp.next
        print('key: ', key, 'map: ', self.map)
        if prev_node: 
            prev_node.next = next_node
            next_node.prev = prev_node
            self.newest.next = tmp
            tmp.prev = self.newest
            self.newest = tmp
        else: 
            self.oldest = next_node
            tmp.next.prev = None
            tmp.next = None
            self.newest.next = tmp
            tmp.prev = self.newest
            self.newest = tmp
        return self.map[key].val
                    
    def put(self, key: int, value: int) -> None:
        if key in self.map: 
            if len(self.map.keys()) == 1: 
                self.map[key] = Node(key, value)
                return 
            if self.newest.key == key: 
                next_newest = self.newest.prev
                next_newest.next = None
                self.newest.prev = None
                self.newest = next_newest
            elif self.oldest.key == key: 
                next_oldest = self.oldest.next
                next_oldest.prev = None
                self.oldest.next = None
                self.oldest = next_oldest
            else: 
                curr = self.map[key]
                prev_node = curr.prev
                next_node = curr.next
                prev_node.next = next_node
                next_node.prev = prev_node
                del map[curr.key]     
            return 
        new_node = Node(key, value)
        if self.size < self.capacity: 
            if self.size == 0: 
                self.oldest = new_node
                self.newest = new_node
            else: 
                self.newest.next = new_node
                new_node.prev = self.newest
                self.newest = self.newest.next
            self.size += 1
        else: 
            self.newest.next = new_node
            new_node.prev = self.newest
            next_oldest = self.oldest.next
            self.oldest.next.prev = None
            self.oldest.next = None
            del self.map[self.oldest.key]
            self.oldest = next_oldest
            self.newest = new_node
        self.map[key] = new_node
        return
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)