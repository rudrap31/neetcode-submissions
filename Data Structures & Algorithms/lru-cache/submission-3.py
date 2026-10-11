class Node:
    def __init__(self, val: int, next: 'Node' = None, prev: 'Node' = None, mapv: int = None):
        self.val = val
        self.next = next
        self.prev = prev
        self.mapv = mapv

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cursize = 0
        self.mp = {}
        self.dummy = Node(0)
        self.cur = None
        return
        

    def get(self, key: int) -> int:
        if key in self.mp:
            val = self.mp[key].val
            if self.mp[key] == self.cur:
                return val
            l = self.mp[key].prev
            r = self.mp[key].next
            if l:
                l.next = r
            if r:
                r.prev = l
            self.mp[key].prev = self.cur
            self.mp[key].next = None
            self.cur.next = self.mp[key]
            self.cur = self.mp[key]

            return val
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.mp[key].val = value

            if self.mp[key] == self.cur:
                return

            l = self.mp[key].prev
            r = self.mp[key].next
            if l:
                l.next = r
            if r:
                r.prev = l
            
            self.mp[key].prev = self.cur
            self.mp[key].next = None
            self.cur.next = self.mp[key]
            self.cur = self.mp[key]
            
            return
        
        else:
            if self.cursize < self.size:
                if self.cur:
                    self.mp[key] = Node(value, None, self.cur, key)
                    self.cur.next = self.mp[key]
                    self.cur = self.mp[key] 
                else:
                    self.mp[key] = Node(value, None, self.dummy, key)
                    self.dummy.next = self.mp[key]
                    self.cur = self.mp[key]
                self.cursize += 1
            else:
                nx = self.dummy.next.next
                dele = self.dummy.next
                
                self.dummy.next = nx 
                if nx:
                    nx.prev = self.dummy 
                if dele == self.cur:
                    self.cur = self.dummy
                self.mp[key] = Node(value, None, self.cur, key)
                self.cur.next = self.mp[key]
                self.cur = self.mp[key]
                del self.mp[dele.mapv]
                del dele
            return


        
