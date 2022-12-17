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
    


def checkHorizontal(sensors,x_init,y,step):
    x=x_init
    delta=[[],[]]
    def allDistancesIncrease(delta):
        if len(delta[0])+len(delta[1])==0 or len(delta[0])!=len(delta[1]):
            return False
        for i in range(len(delta[0])):
            if delta[0][i]<=delta[1][i]:
                return False
        return True
    
    covered = set()
    beacons = [pos.pos_beacon for pos in sensors]
            
    found = True
    x=x_init-step
    while found or not allDistancesIncrease(delta):
        x=x+step
        found = False
        pos = (x,y)
        delta[x%2]=[x.compute_distance(pos) for x in sensors]
        if pos in beacons:
            found = True
            continue
        for sensor in sensors:
            if sensor.is_pos_covered(pos):
                found=True
                covered.add(pos)
                break
        
        
    return len(covered)

pattern = r"=(-?[0-9]+)"
sensors= []

with open("input.txt") as f:
    for line in f:
        line = line.strip().replace("\n","")
        sensor_data = [int(x) for x in re.findall(pattern,line)]
        sensors.append(Sensor((sensor_data[0],sensor_data[1]),(sensor_data[2],sensor_data[3])))
            

Y=2000000
#Y=10



solution = checkHorizontal(sensors,1,Y,1) + checkHorizontal(sensors,0,Y,-1)

print(str(solution))