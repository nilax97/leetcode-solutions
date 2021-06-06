class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = []
        self.mod = 1000
        for i in range(self.mod):
            self.val.append([])
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        x = key % self.mod
        for i in range(len(self.val[x])):
            if self.val[x][i][0] == key:
                self.val[x][i][1] = value
                return
        self.val[x].append([key,value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        x = key % self.mod
        for i in range(len(self.val[x])):
            if self.val[x][i][0] == key:
                return self.val[x][i][1]
        return -1
        
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        x = key % self.mod
        for i in range(len(self.val[x])):
            if self.val[x][i][0] == key:
                self.val[x].pop(i)
                return
        return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
