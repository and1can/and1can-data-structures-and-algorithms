from collections import defaultdict
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        curr = head
        hashMap = defaultdict(lambda: None)
        while (curr):
            if curr not in hashMap: 
                hashMap[curr] = Node(curr.val, None, None)
            if curr.next != None: 
                if curr.next not in hashMap: 
                    hashMap[curr.next] = Node(curr.next.val, None, None)
                hashMap[curr].next = hashMap[curr.next]
            else: 
                hashMap[curr].next = None
            if curr.random != None: 
                if curr.random not in hashMap: 
                    hashMap[curr.random] = Node(curr.random.val, None, None)
                hashMap[curr].random = hashMap[curr.random]
            else: 
                hashMap[curr].random = None
            curr = curr.next
        return hashMap[head]