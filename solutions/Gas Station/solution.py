class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def check(start, price):
            val = 0
            n = len(price)
            for i in range(n):
                val += price[(start+i) % n]
                if val < 0:
                    return 0
            return 1
        n = len(gas)
        price = [0] * n
        for i in range(n):
            price[i] = gas[i] - cost[i]
        for i in range(n):
            if price[i] >= 0:
                ret = check(i,price)
                if ret == 1:
                    return i
        return -1
