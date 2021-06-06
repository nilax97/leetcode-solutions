class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        # print(trips)
        for i in range(len(trips)):
            trip = trips[i]
            for j in range(i):
                if trips[j][2] <= trip[1]:
                    capacity += trips[j][0]
                    trips[j][0] = 0
            # print(capacity)
            capacity -= trip[0]
            if capacity < 0:
                return False
        return True
