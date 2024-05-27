from UniqueLinkedList import UniqueLinkedList

class LinearProbingHashTable:
    def __init__(self, MINBUCKETS=2, MINLOADFACTOR=0.1, MAXLOADFACTOR=0.9):
        """initializes the linear prboing hash table"""
        if MAXLOADFACTOR >= 1:
            raise ValueError("MAXLOADFACTOR must be less than 1")
        self.MINBUCKETS = MINBUCKETS
        self.MINLOADFACTOR = MINLOADFACTOR
        self.MAXLOADFACTOR = MAXLOADFACTOR
        self.keys = [None] * self.MINBUCKETS
        self.values = [None] * self.MINBUCKETS
        self.num_items = 0
    
    def __len__(self):
        """return the number of items in the hash table"""
        return self.num_items
    
    def __setitem__(self, key, value):
        """adds an item to the hash table"""
        if (self.num_items + 1) / self.MINBUCKETS > self.MAXLOADFACTOR:
            self._rehash(self.MINBUCKETS * 2)

        index = hash(key) % self.MINBUCKETS
        while self.keys[index] is not None and self.keys[index] != -1:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.MINBUCKETS
        self.keys[index] = key
        self.values[index] = value
        self.num_items += 1

    def __getitem__(self, key):
        """returns the value associated with the given key"""
        index = hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.MINBUCKETS
        
        raise KeyError(key)
    
    def __contains__(self, key):
        """returns a boolean for whether the key is in the has table"""
        index = hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return True
            index = (index + 1) % self.MINBUCKETS
        
        return False
    
    def pop(self, key):
        """removes the item with the given key"""
        index = hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                r_val = self.values[index]
                self.keys[index] = -1
                self.values[index] = None
                self.num_items -= 1
                return r_val
            index = (index + 1) % self.MINBUCKETS
        raise KeyError(key)

    def get_loadfactor(self):
        """returns the load factor"""
        return self.num_items / self.MINBUCKETS
    
    
    def _rehash(self, new_size):
        """resizes the hash table"""
        old_keys = self.keys
        old_values = self.values
        self.keys = [None] * new_size
        self.values = [None] * new_size
        self.MINBUCKETS = new_size
        self.num_items = 0
        for i in range(len(old_keys)):
            if old_keys[i] is not None and old_keys[i] != -1:
                self.__setitem__(old_keys[i], old_values[i])