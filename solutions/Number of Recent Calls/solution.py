class RecentCounter:

    def __init__(self):
        self.ans = list()

    def ping(self, t: int) -> int:
        self.ans.append(t)
        for i in range(len(self.ans)-1,-1,-1):
            if self.ans[i] < (t-3000):
                return len(self.ans) - i - 1
        return len(self.ans)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
