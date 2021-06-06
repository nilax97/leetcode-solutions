class FirstUnique:

    def __init__(self, nums: List[int]):
        self.store = list()
        self.values = dict()
        for x in nums:
            if x in self.values:
                self.values[x] += 1
            else:
                self.values[x] = 1
        for x in nums:
            if self.values[x] == 1:
                self.store.append(x)

    def showFirstUnique(self) -> int:
        if len(self.store) == 0:
            return -1
        return self.store[0]
        

    def add(self, value: int) -> None:
        if value in self.values and self.values[value]==1:
            for i in range(len(self.store)):
                if self.store[i]==value:
                    self.store.pop(i)
                    break
            self.values[value] += 1
        elif value not in self.values:
            self.values[value] = 1
            self.store.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
