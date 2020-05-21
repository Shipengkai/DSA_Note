class HashTable():
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def hashfunction(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash+1) % self.size

    def put(self, key, data):
        key_hash = self.hashfunction(key)
        unfinished = True
        count = 0
        while unfinished:
            if self.slots[key_hash] is None:
                self.slots[key_hash], self.data[key_hash] = key, data
                unfinished = False
            elif self.slots[key_hash] == key:
                self.data[key_hash] = data  # update
                unfinished = False
            else:
                key_hash = self.rehash(key_hash)
                count += 1
            if count > self.size - 1:
                print("don't have available slot")
                break

    def get(self, key):
        key_hash = self.hashfunction(key)
        count = 0
        data = None
        while count < self.size:
            if self.slots[key_hash] == key:
                data = self.slots[key_hash]
                print(f'{key}: {self.data[key_hash]}')
                return
            elif self.slots[key_hash] is None:
                print(False)
                return
            else:
                count = 0
                key_hash = self.rehash(key_hash)
                count += 1
            if count > self.size - 1:
                print("False...")
                break
        return data


if __name__ == "__main__":
    ht = HashTable()
    ht.put(1, 'one')
    ht.put(2, 'two')
    ht.get(1)
    ht.get(2)
