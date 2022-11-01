from math import *

result = 0
n, m = map(int, input().split())
x  = list(map(int, input().split()))
times = []
for val in x:
    times.append(int(pow(2,val)))

worker_times = []
for i in range(m):
    worker_times.append(0)
for time in times:
    for i in range(len(worker_times)):
        for j in range(len(worker_times)):
            if(i != j and worker_times[i] + time > worker_times[j]):
                worker_times[i] += time

print(worker_times)

print(result % (pow(10,9) + 7))