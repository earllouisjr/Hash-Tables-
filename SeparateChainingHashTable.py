from UniqueLinkedList import UniqueLinkedList

class SeparateChainingHashTable:
    def __init__(self, MINBUCKETS=2, MINLOADFACTOR=0.5, MAXLOADFACTOR=1.5):
        """"""
        self.MINBUCKETS = MINBUCKETS
        self.MINLOADFACTOR = MINLOADFACTOR
        self.MAXLOADFACTOR = MAXLOADFACTOR
        self.buckets = [UniqueLinkedList() for i in range(MINBUCKETS)]
        self.num_items = 0
    
    def __len__(self):
        """returns the length of the hash table"""
        return self.num_items
    
    def __setitem__(self, key, value):
        """sets the item at the given key to the given value"""
        index = hash(key) % len(self.buckets)
        self.num_items += self.buckets[index].add(key, value)
        if self.get_loadfactor() > self.MAXLOADFACTOR:
            self._rehash(2 * len(self.buckets))
    
    def __getitem__(self, key):
        """returns the item with the given key"""
        index = hash(key) % len(self.buckets)
        return self.buckets[index].get(key)

    def __contains__(self, key):
        """checks if the given key is in the hash table"""
        index = hash(key) % len(self.buckets)
        return key in self.buckets[index]

    def pop(self, key):
        """removes the node with the given key"""
        index = hash(key) % len(self.buckets)
        value = self.buckets[index].remove(key)
        self.num_items -= 1
        return value
    
    def get_loadfactor(self):
        """returns the current load factor"""
        return self.num_items/len(self.buckets)

    def _rehash(self, new_size):
        """resizes the hash table when the load factor is >1.5"""
        old_buckets = self.buckets
        self.buckets = [UniqueLinkedList() for i in range(new_size)]
        self.num_items = 0
        for bucket in old_buckets:
            current = bucket._head
            while current:
                self.__setitem__(current.key, current.value)
                current = current.link