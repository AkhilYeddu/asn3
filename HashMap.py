class LinearProbingHashmap:
    def __init__(self, capacity=11):
        self.capacity=capacity
        self.size=0
        self.table=[None]*capacity

    def _hash(self, key):
        return hash(key)%self.capacity

    def _probe(self, key, i):
        return (self._hash(key)+i)%self.capacity

    def insert(self, key, value):
        index=self._hash(key)
        for i in range(self.capacity):
            probe_index=self._probe(key, i)
            if self.table[probe_index] is None or self.table[probe_index][0]==key:
                self.table[probe_index]=(key, value)
                self.size+=1
                return
        raise Exception("Hashmap is full")

    def find(self, key):
        index = self._hash(key)
        for i in range(self.capacity):
            probe_index = self._probe(key, i)
            if self.table[probe_index] is None:
                return False
            if self.table[probe_index][0]==key:
                return True
        return False
    def remove(self, key):
        index=self._hash(key)
        for i in range(self.capacity):
            probe_index=self._probe(key, i)
            if self.table[probe_index] is None:
                return
            if self.table[probe_index][0]==key:
                self.table[probe_index]=None
                self.size-=1
                return
        raise KeyError(f"Key {key} not found")

    def __repr__(self):
        return str(self.table)