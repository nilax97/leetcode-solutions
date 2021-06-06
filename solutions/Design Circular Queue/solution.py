class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.back = 0
        self.front = 0
        self.size = 0
        self.n = k

    def enQueue(self, value: int) -> bool:
        if self.size == self.n:
            return False
        self.q[self.back % self.n] = value
        self.size += 1
        self.back += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.front += 1
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.q[self.front % self.n]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.q[(self.back-1) % self.n]
        
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.n
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
