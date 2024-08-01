class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head=self.Node(0, 0)
        self.tail=self.Node(0, 0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def _remove(self, node: Node):
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node

    def _add(self, node: Node):
        next_node=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next=next_node
        next_node.prev= node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self._remove(node)
            self._add(node)
        else:
            if self.size==self.capacity:
                lru= self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
                self.size -= 1
            new_node= self.Node(key, value)
            self._add(new_node)
            self.cache[key]= new_node
            self.size += 1

