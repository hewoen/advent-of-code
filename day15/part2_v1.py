import re

def mannhattan_distance(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


class Sensor:  
    def __init__(self,pos,pos_closest_beacon):
        self._pos = pos
        self._pos_closest_beacon = pos_closest_beacon
        self._manhattan_distance = mannhattan_distance(pos,pos_closest_beacon)
        
    def compute_distance(self, pos):
        return mannhattan_distance(self._pos, pos)
    
    def is_pos_covered(self, pos):
        return self.compute_distance(pos) <= self._manhattan_distance
    
    def is_beacon_at_pos(self, pos):
        return pos==self._pos_closest_beacon
    
    @property
    def pos_beacon(self):
        return self._pos_closest_beacon
    
    
    @property
    def pos(self):
        return self._pos
    


def findGap(sensors,limit):
    delta=[[],[]]
    
    covered = set()
    beacons_sensors = [pos.pos_beacon for pos in sensors] + [sensor.pos for sensor in sensors]
            
    found = True
    for y in range(limit+1):
        for x in range(limit+1):
            if (x,y) not in beacons_sensors:
                covered.clear()
                chk = [(x,y),(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
                for sensor in sensors:
                    for c in chk:
                        if sensor.is_pos_covered(c):
                            covered.add(c)
            
                if (x,y) not in covered and len(covered)==4:
                    return (x,y)
            
            
                    
                    

pattern = r"=(-?[0-9]+)"
sensors= []

with open("input.txt") as f:
    for line in f:
        line = line.strip().replace("\n","")
        sensor_data = [int(x) for x in re.findall(pattern,line)]
        sensors.append(Sensor((sensor_data[0],sensor_data[1]),(sensor_data[2],sensor_data[3])))
            

#LIMIT=20
LIMIT=4000000



solution = findGap(sensors, LIMIT)

print(str(solution[0]*4000000+solution[1]))