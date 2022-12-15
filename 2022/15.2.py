a="""Sensor at x=3291456, y=3143280: closest beacon is at x=3008934, y=2768339
Sensor at x=3807352, y=3409566: closest beacon is at x=3730410, y=3774311
Sensor at x=1953670, y=1674873: closest beacon is at x=2528182, y=2000000
Sensor at x=2820269, y=2810878: closest beacon is at x=2796608, y=2942369
Sensor at x=3773264, y=3992829: closest beacon is at x=3730410, y=3774311
Sensor at x=2913793, y=2629579: closest beacon is at x=3008934, y=2768339
Sensor at x=1224826, y=2484735: closest beacon is at x=2528182, y=2000000
Sensor at x=1866102, y=3047750: closest beacon is at x=1809319, y=3712572
Sensor at x=3123635, y=118421: closest beacon is at x=1453587, y=-207584
Sensor at x=2530789, y=2254773: closest beacon is at x=2528182, y=2000000
Sensor at x=230755, y=3415342: closest beacon is at x=1809319, y=3712572
Sensor at x=846048, y=51145: closest beacon is at x=1453587, y=-207584
Sensor at x=3505756, y=3999126: closest beacon is at x=3730410, y=3774311
Sensor at x=2506301, y=3745758: closest beacon is at x=1809319, y=3712572
Sensor at x=1389843, y=957209: closest beacon is at x=1453587, y=-207584
Sensor at x=3226352, y=3670258: closest beacon is at x=3730410, y=3774311
Sensor at x=3902053, y=3680654: closest beacon is at x=3730410, y=3774311
Sensor at x=2573020, y=3217129: closest beacon is at x=2796608, y=2942369
Sensor at x=3976945, y=3871511: closest beacon is at x=3730410, y=3774311
Sensor at x=107050, y=209321: closest beacon is at x=1453587, y=-207584
Sensor at x=3931251, y=1787536: closest beacon is at x=2528182, y=2000000
Sensor at x=1637093, y=3976664: closest beacon is at x=1809319, y=3712572
Sensor at x=2881987, y=1923522: closest beacon is at x=2528182, y=2000000
Sensor at x=3059723, y=2540501: closest beacon is at x=3008934, y=2768339"""

test='''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''

#a=test

#parse input
sensors = []
for line in a.splitlines():
    sensor_str, beacon_str = line.split(": ")
    x, y = [int(x) for x in sensor_str.split("x=")[1].split(", y=")]
    sensor = [x,y]
    x, y = [int(x) for x in beacon_str.split("x=")[1].split(", y=")]
    beacon = [x,y]
    sensors.append({"sensor": sensor, "beacon": beacon})

#calculate each sensor's manhattanDistance to its beacon
def manhattanDistance(c1,c2):
    x1,y1 = c1
    x2,y2 = c2
    return abs(x1 - x2) + abs(y1 - y2)

for sensor in sensors: sensor['distance'] = manhattanDistance(sensor['sensor'],sensor['beacon'])

#get minimum and maximum x and y values
sensorMinX = sorted(sensors,key=lambda x: x['sensor'][0] - x['distance'])[0]
sensorMinY = sorted(sensors,key=lambda x: x['sensor'][1] - x['distance'])[0]
sensorMaxX = sorted(sensors,key=lambda x: x['sensor'][0] + x['distance'])[-1]
sensorMaxY = sorted(sensors,key=lambda x: x['sensor'][1] + x['distance'])[-1]
min_x = sensorMinX['sensor'][0] - sensorMinX['distance']
min_y = sensorMinY['sensor'][1] - sensorMinY['distance']
max_x = sensorMaxX['sensor'][0] + sensorMaxX['distance']
max_y = sensorMaxY['sensor'][1] + sensorMaxY['distance']
print(min_x,max_x,min_y,max_y)

def checkCell(x,y):
    if (0 <= x <= boxBounds and 0 <= y <= boxBounds):
        noneFound=True
        for sensor in sensors:
            if manhattanDistance(sensor['sensor'],(x,y)) <= sensor['distance']: 
                noneFound = False
                break
            if sensor["beacon"] == [x,y]: 
                noneFound = False
                break
        if noneFound: print(f"answer = {x*4000000 + y}") #part 2 Answer########################################

#boxBounds=20 #test
boxBounds=4000000 #prod
for sensorNum,sensor in enumerate(sensors):
    print(f"perimeter checking sensor {sensorNum}")
    distance = sensor['distance']+1 # +1 because it's one square out from the edge of the beacon
    sensorX = sensor['sensor'][0]
    sensorY = sensor['sensor'][1]
    min_xVertex = sensorX - distance
    max_xVertex = sensorX + distance
    min_yVertex = sensorY - distance
    max_yVertex = sensorY + distance

    #check every cell on the perimeter of the sensor (diamond shape)
    y=sensorY
    for dy in range(-1,2,2):
        for i,x in enumerate(range(min_xVertex, max_xVertex+1)):
            checkCell(x,y)
            if x <= sensorX: y -= dy    #left vertex to top/bottom vertex
            else: y += dy               #top/bottom vertex to right vertex