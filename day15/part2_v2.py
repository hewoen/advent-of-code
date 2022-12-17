import re
import time

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
    def covered_distance(self):
        return self._manhattan_distance
    
    @property
    def pos_beacon(self):
        return self._pos_closest_beacon
    
    
    @property
    def pos(self):
        return self._pos



def computePosCircle(pos,d):
    positions = []
    x=d
    y=0
    while x>=0:
        positions.append((pos[0]+x,pos[1]+y))
        positions.append((pos[0]-x,pos[1]+y)) #Spiegeln zur X-Achse
        positions.append((pos[0],pos[1]-y)) #Spiegeln zur Y-Achse
        positions.append((pos[0]-x,pos[1]-y)) #Spiegeln zur X- und Y-Achse
        x=x-1
        y=y-1
    return positions


def findGap(sensors,limit):
    covered = set()
    not_covered=set()
    beacons_sensors = [pos.pos_beacon for pos in sensors] + [sensor.pos for sensor in sensors]
    
    def is_covered(sensors,covered:set,not_covered:set, pos):
        if pos in covered:
                return True
        if pos in not_covered:
            return False
        for sensor in sensors:
            if sensor.is_pos_covered(pos):
                covered.add(pos)
                return True
        not_covered.add(pos)
        return False
        
    for sensor in sensors:
        for pos in computePosCircle(sensor.pos,sensor.covered_distance+1):
            
            if pos==pos[0] > limit  or pos[0]<0 or pos[1]>limit or pos[1]<0 or pos in beacons_sensors or is_covered(sensors,covered,not_covered,pos):
                continue
            matches=0
            x,y = pos
            if not is_covered(sensors,covered,not_covered,pos):
                chk = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
                for c in chk:
                    if is_covered(sensors,covered,not_covered,c):
                        matches=matches+1
            
                if matches==4:
                    return pos
            
            
            
                    
                    

pattern = r"=(-?[0-9]+)"
sensors= []

INPUT = "input.txt"
#INPUT = "input_example.txt"

with open(INPUT) as f:
    for line in f:
        line = line.strip().replace("\n","")
        sensor_data = [int(x) for x in re.findall(pattern,line)]
        sensors.append(Sensor((sensor_data[0],sensor_data[1]),(sensor_data[2],sensor_data[3])))
            

#LIMIT=20
LIMIT=4000000



solution = findGap(sensors, LIMIT)

print(str(solution[0]*4000000+solution[1]))
print("Execution time: " + str(time.process_time()) + " Seconds")