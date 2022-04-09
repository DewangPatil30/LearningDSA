"""
Finally Did it 💖💖💖💖💖💖💖💖💖💖💖💖

Approach: Please understand from video:-

LeetCode 146: https://leetcode.com/problems/lru-cache/
YT: https://www.youtube.com/watch?v=xDEuM5qa0zg
"""

class ListNode:
    def __init__(self, key = -9999, val=-9999, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt
        
class Dlist:
    def __init__(self, key=-9999, val = -9999, prev = None, nxt = None):
        self.head = ListNode(key, val, prev, nxt)
        self.tail = ListNode(key, val, prev, nxt)
        
    def connectEnds(self):
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def delete_lru(self):
        key = self.tail.prev.key
        temp = self.tail.prev.prev
        temp.next = self.tail
        self.tail.prev = temp
        
        return key


class LRUCache:

    def __init__(self, capacity: int):
        self.m = {}
        
        self.dlst = Dlist()
        self.dlst.connectEnds()
        
        self.cap = capacity
        
        
    def updateRecent(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
        node = ListNode(node.key, node.val)
        head = self.dlst.head
        
        node.next = head.next
        node.next.prev = node
        node.prev = head
        head.next = node
        
        return node
      
        
    def addRecent(self,key, val):
        node = ListNode(key, val)
        head = self.dlst.head
        
        node.next = head.next
        node.next.prev = node
        node.prev = head
        head.next = node
        
        return node
        
        
    def get(self, key: int) -> int:
        
        if key not in self.m: return -1
        self.m[key] = self.updateRecent(self.m[key])
        return self.m[key].val

      
    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.m[key].val = value
            self.m[key] = self.updateRecent(self.m[key])
            return
        
        if len(self.m) == self.cap:
            self.m.pop(self.dlst.delete_lru())

        self.m[key] = self.addRecent(key, value)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
