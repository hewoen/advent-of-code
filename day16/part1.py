import re
import time

class Valve:
    def __init__(self,label,flow_rate,tunels):
        self._label = label
        self._tunnels = tunels
        self._flow_rate = flow_rate
        self._opened = False
    
    

        
    
    @property
    def open(self):
        return self._opened
    
    def open_it(self):
        self._opened=True
    
    @property
    def flow_rate(self):
        return self._flow_rate
    
    @property
    def label(self):
        return self._label
    
    @property
    def tunnels(self):
        return self._tunnels
    
    def setTunnels(self,tunnels):
        self._tunnels = tunnels

     
def find_path(a:Valve, b:Valve):
    q=[a]
    visited=[]
    distance={a.label:0}
    if a.label==b.label:
        return 0
    
    while len(q)>0:
        node = q.pop(0)
        visited.append(node.label)
        for neighbour in node.tunnels:
            d = distance[node.label]+1
            if neighbour.label==b.label:
                return d
            elif neighbour.label not in visited:
                q.append(neighbour)
                distance.update({neighbour.label:d})

        
    
    raise Exception("There is no path from ")
        
def get_pressure(start:Valve, minutes_left:int, valves=[]):
    if minutes_left <=0:
        return 0
    
    
    minutes_left=minutes_left-1
    pressure = minutes_left*start.flow_rate
    
    max=0
    for valve in valves:
        new_valve_selection = [v for v in valves if v.label!=valve.label]
        distance = find_path(start,valve)
        if (c:=get_pressure(valve,minutes_left-distance,new_valve_selection)) > max:
            max=c
    
    return pressure+max
    
        


        
            
            
    
    
        

def determine_route(start:Valve, time_limit):
    steps = time_limit/2
    

INPUT = "input.txt"
#INPUT = "input_example.txt"
#INPUT = "input_example2.txt"
MINUTES = 30



start_valve = "AA"

pattern = r"Valve ([A-Z]{2}).+rate=([0-9]+).+valves? ([A-Z, ]+)"
with open(INPUT) as f:
    graph = {}
    for line in f:
        line = line.strip().replace("\n","")
        v = re.match(pattern,line)
        graph.update({v.group(1):Valve(v.group(1),int(v.group(2)),v.group(3).split(","))})
    
    for valve in graph.values():
        valve.setTunnels([graph[x.strip()] for x in valve.tunnels])
    start_valve = graph[start_valve]
    


valves_without_zero = [v for v in graph.values() if v.flow_rate>0]
solution = get_pressure(start_valve,MINUTES+1,valves_without_zero)

print(str(solution))
print("Execution time: " + str(time.process_time()) + " Seconds")