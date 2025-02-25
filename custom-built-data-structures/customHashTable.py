class HashTable():
    def __init__(self, size):
        self.data = [None] * size

    def hash(self, key):
        return hash(key) % len(self.data)  # Python's built-in hash function
    
    def set(self, key, value):
        address = self.hash(key)
        item = [key, value]

        if self.data[address] is None:
            self.data[address] = []

        self.data[address].append(item)

        return self.data
    
    def get(self, key):
        address = self.hash(key)
        currentBucket = self.data[address]

        if currentBucket:
            for i in range(len(currentBucket)):
                if currentBucket[i][0] == key:
                    return currentBucket[i][1]

        return None

newHashTable = HashTable(50)


newHashTable.set('grapes', 10000)
newHashTable.set('apples', 1000)
newHashTable.set('mangoes', 1000)
newHashTable.set('beer', 100)

print(newHashTable)

print(newHashTable.get('grapes'))
print(newHashTable.get('apples'))
print(newHashTable.get('mangoes'))
print(newHashTable.get('beer'))

