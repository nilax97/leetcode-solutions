class UndergroundSystem:

    def __init__(self):
        self.customers_time = dict()
        self.customers_station = dict()
        self.total_time = dict()
        self.count = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers_time[id] = t
        self.customers_station[id] = stationName
            
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station = self.customers_station[id]
        time = self.customers_time[id]
        if (station + stationName) in self.total_time:
            self.total_time[station + stationName] += t - time
            self.count[station + stationName] += 1
        else:
            self.total_time[station + stationName] = t - time
            self.count[station + stationName] = 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        station = startStation + endStation
        return self.total_time[station] / self.count[station]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
