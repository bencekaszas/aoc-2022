from scipy.spatial.distance import cityblock
from parse import *
import numpy as np
from collections import defaultdict

lines = open('input/15').readlines()

S = []
B = []
l = defaultdict(int)
r_min = []
c_min = []
r_max = []
c_max = []


for line in lines:
    s,b = line.split(': ')
    sensor = parse('Sensor at x={:d}, y={:d}', s)
    beacon = parse('closest beacon is at x={:d}, y={:d}\n', b)
    S.append(sensor.fixed)
    l[sensor.fixed] = cityblock(sensor.fixed,beacon.fixed)
    B.append(beacon.fixed)
    r_min.append(sensor[1]- l[sensor.fixed])
    r_min.append(beacon[1])
    c_min.append(sensor[0] - l[sensor.fixed])
    c_min.append(beacon[0])
    r_max.append(sensor[1]+ l[sensor.fixed])
    r_max.append(beacon[1])
    c_max.append(sensor[0] + l[sensor.fixed])
    c_max.append(beacon[0])

r_sz = abs(min(r_min)) + max(r_max)
c_sz = abs(min(c_min)) + max(c_max)



checked = [0 for _ in range(c_sz)]

#print((checked))

for sensor in S:
    if abs(sensor[1] - 2000000) < l[sensor]:
        #print('sensor: ',sensor, l[sensor])
        dist = (l[sensor] - abs(sensor[1] - 2000000))
        #print(dist)
        checked[sensor[0]-min(c_min)-dist:sensor[0]-min(c_min)+dist+1] = [1 for _ in range(2*dist+1)]
        #print(sensor[0]-dist,sensor[0]+dist+1)
        #print(checked)

#print(len(checked))

s = 0
for beacon in list(set(B)):
    if beacon[1] == 2000000: s+= 1
for sensor in S:
    if sensor[1] == 2000000: s+= 1

print(sum(checked)-s)

