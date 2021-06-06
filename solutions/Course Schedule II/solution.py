class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        valid = [1] * numCourses
        val = dict()
        for x in prerequisites:
            if x[0] in val:
                val[x[0]].append(x[1])
            else:
                val[x[0]] = [x[1]]
            valid[x[0]] = 0
        for i in range(numCourses):
            if valid[i] == 1:
                order.append(i)
        while(True):
            change = 0
            for i in range(numCourses):
                random = 0
                if valid[i] == 1:
                    continue
                for x in val[i]:
                    if valid[x] == 0:
                        random = 1
                        break
                if random == 0:
                    change += 1
                    valid[i] = 1
                    order.append(i)
            if change == 0:
                break
        for x in valid:
            if x==0:
                return []
        return order
