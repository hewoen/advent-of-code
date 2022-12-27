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


cache = {} # (minutes_remaining, position,opened valves)
     
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
    
    state = (minutes_left,start.label,"".join([v.label for v in valves]))
    if state in cache.keys():
        return cache[state]
    
    pressure = minutes_left*start.flow_rate
    
    max=0
    for valve in valves:
        new_valve_selection = [v for v in valves if v.label!=valve.label]
        distance = find_path(start,valve)
        if (c:=get_pressure(valve,minutes_left-distance,new_valve_selection)) > max:
            max=c
    
    result = pressure+max
    cache[state]=result
    return result
    
        
k=15
n=7
combinations = [[] for _ in range(n)]
for i in range(1,pow(2,k)):
    combination = 0
    count=0
    for j in range(k):
        c=1<<(j)
        if c&i != 0:
            combination=combination|c
            count = count+1
    if count > n:
        continue
    combinations[count-1].append(combination)
    

for i,c in enumerate(combinations):
    print(str(i+1)+":" + str(len(c)))
    

INPUT = "input.txt"
#INPUT = "input_example.txt"
#INPUT = "input_example2.txt"
MINUTES = 26

def complement(valves):
    valves_labels = [v.label for v in valves]
    return [v for v in valves_without_zero if v.label not in valves_labels]

def create_valve_list(bitstring,all_valves,k):
    valves = []
    for i in range(k):
        c=1<<i
        if bitstring&c != 0:
            valves.append(all_valves[i])
    return valves

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
# for i in range(5):
#     valves_without_zero.pop(0)

solution = 0
for i in range(6,len(combinations)):
    print(i)
    for bitstring in combinations[i]:
        valves=create_valve_list(bitstring,valves_without_zero,k)
        c1=get_pressure(start_valve,MINUTES+1,valves)
        #cache.clear()
        c2=get_pressure(start_valve,MINUTES+1,complement(valves))
        #cache.clear()
        solution = max(solution,c1+c2)

print(str(solution))
print("Execution time: " + str(time.process_time()) + " Seconds")