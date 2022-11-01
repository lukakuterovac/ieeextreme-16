testcases = int(input())

for i in range(testcases):
    stations = []
    line = list(map(int, input().split()))
    stations_count = line.pop(0)
    station = line
    stations.append(station)
    for j in range(stations_count - 1):
        station = list(map(int, input().split()))
        stations.append(station)
    cost = stations[0][0] * stations[0][1]
    fuel = stations[0][0]
    for j in range(1, stations_count):
        fuel -= stations[j][0]
        if(j < stations_count and stations[j + 1][0] > fuel):
            cost += (stations[0][0] - fuel) * stations[j][1]
            fuel = stations[0][0]
    print(cost)
