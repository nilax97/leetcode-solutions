class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        to_visit = [[0,0,0,0,0]]
        if target == "0000":
            return 0
        visited = dict()
        dead = dict()
        for x in deadends:
            dead["".join(str([int(x[0]),int(x[1]),int(x[2]),int(x[3])]))] = 1
            visited["".join(str([int(x[0]),int(x[1]),int(x[2]),int(x[3])]))] = 1
        tar = [int(target[0]),int(target[1]),int(target[2]),int(target[3])]
        while(len(to_visit) != 0):
            x = to_visit.pop(0)
            if "".join(str(x[0:4])) in dead:
                continue
            nbrs = []
            nbrs.append([(x[0] + 1) % 10, (x[1] + 0) % 10, (x[2] + 0) % 10, (x[3] + 0) % 10, x[4] + 1])
            nbrs.append([(x[0] + 0) % 10, (x[1] + 1) % 10, (x[2] + 0) % 10, (x[3] + 0) % 10, x[4] + 1])
            nbrs.append([(x[0] + 0) % 10, (x[1] + 0) % 10, (x[2] + 1) % 10, (x[3] + 0) % 10, x[4] + 1])
            nbrs.append([(x[0] + 0) % 10, (x[1] + 0) % 10, (x[2] + 0) % 10, (x[3] + 1) % 10, x[4] + 1])
            nbrs.append([(x[0] - 1) % 10, (x[1] + 0) % 10, (x[2] + 0) % 10, (x[3] + 0) % 10, x[4] + 1])
            nbrs.append([(x[0] + 0) % 10, (x[1] - 1) % 10, (x[2] + 0) % 10, (x[3] + 0) % 10, x[4] + 1])
            nbrs.append([(x[0] + 0) % 10, (x[1] + 0) % 10, (x[2] - 1) % 10, (x[3] + 0) % 10, x[4] + 1])
            nbrs.append([(x[0] + 0) % 10, (x[1] + 0) % 10, (x[2] + 0) % 10, (x[3] - 1) % 10, x[4] + 1])
            for y in nbrs:
                if y[0:4] == tar:
                    return y[4]
                elif "".join(str(y[0:4])) in dead:
                    pass
                elif "".join(str(y[0:4])) in visited:
                    pass
                else:
                    to_visit.append(y)
                visited["".join(str(y[0:4]))] = 1
        return -1