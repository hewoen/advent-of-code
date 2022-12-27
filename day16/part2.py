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
        
def get_pressure(players,minutes_left, valves=[]):
    #player: (destination,remaining_minutes)
    if minutes_left <=0:
        return 0   
    
    minutes_left=minutes_left-1
    max=0
    pressure=0
    available_player=[]
    new_players = []
    
    def create_player(start,dest,minutes_left):
        d=find_path(start,dest)+1
        return (dest,d,(minutes_left-d)*valve.flow_rate)
    
    for i in range(len(players)):
        new_players.append((players[i][0],players[i][1]-1,players[i][2]))
        if new_players[i][1]<=0:
            pressure += players[i][2]
            available_player.append(i)
    players = new_players
    
    options = []
    
    
    
    if len(available_player)==1:
        for valve in valves:
            options.append([create_player(players[available_player[0]][0],valve,minutes_left),players[(available_player[0]+1)%2]])
    elif len(available_player)==2:
        valves2 = valves
        for valve in valves:
            valves2 = [v for v in valves2 if v.label!=valve.label]
            for valve2 in valves2:
                options.append([create_player(players[0][0],valve,minutes_left),create_player(players[1][0],valve2,minutes_left)])
                if players[0][0].label != players[1][0].label:
                    options.append([create_player(players[0][0],valve2,minutes_left),create_player(players[1][0],valve,minutes_left)])
    else:
        return get_pressure(players,minutes_left,valves)
    
    
    for option in options:
        if (c:=get_pressure(option,minutes_left,[v for v in valves if v.label != option[0][0].label and v.label != option[1][0].label]))>max:
            max=c
            
    return pressure+max
    
    
    

#INPUT = "input.txt"
INPUT = "input_example.txt"
#INPUT = "input_example2.txt"
MINUTES = 26



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
players=[(graph["AA"],0,0),(graph["AA"],0,0)]
solution = get_pressure(players,MINUTES+1,valves_without_zero)

print(str(solution))
print("Execution time: " + str(time.process_time()) + " Seconds")