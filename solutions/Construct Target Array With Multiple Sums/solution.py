import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            if target[0] == 1:
                return True
            else:
                return False
        target = [-t for t in target]
        heapq.heapify(target)
        total = -sum(target)
        while True:
            # print(target)
            top = -heapq.heappop(target)
            if top == 1:
                return True
            rest = total - top
            if top <= rest:
                return False
            top = rest if top % rest == 0 else top % rest
            total = rest + top
            heapq.heappush(target, -top)
        return True
