from abc import ABC
from importlib.abc import SourceLoader
INPUT_FILE = "input.txt"

class Direction(ABC):
    def get_cords():
        pass

    def perform_move(pos):
        cords =  Direction.get_cords()
        return (cords[0]+pos[0],cords[1]+pos[1])

class LEFT(Direction):
    def get_cords():
        return (-1,0)

class RIGHT(Direction):
    def get_cords():
        return (1,0)


class UP(Direction):
    def get_cords():
        return (0,-1)

class DOWN(Direction):
    def get_cords():
        return (0,1)


class HighMap:
    def __init__(self,map) -> None:
        self._map = map
        for y,line in enumerate(map):
            for x,column in enumerate(line):
                if column=="S":
                    self._start=(x,y)
                elif column=="E":
                    self._end = (x,y)
    
    @property
    def start(self):
        return self._start
    
    @property
    def end(self):
        return self._end
    
    @property
    def width(self):
        return len(self._map[0])
    
    @property
    def height(self):
        return len(self._map)
    
    def move_possible(self,pos,direction:Direction):
        direction = direction.get_cords()
        new_pos = (pos[0]+direction[0],pos[1]+direction[1])

        if new_pos[0] < 0 or new_pos[0] >= self.width or new_pos[1] < 0 or new_pos[1] >= self.height:
            return False

        elavation_pos = self.pos(pos)
        elavation_new_pos = self.pos(new_pos)

        if elavation_new_pos <= elavation_pos+1:
            return new_pos
        
        return False
        

    def pos(self,pos):
        x,y = pos
        elavation = self._map[y][x]
        if elavation=="S":
            return ord("a")
        elif elavation=="E":
            return ord("z")
        return ord(self._map[y][x])

class Node:
    def __init__(self,pos,distance,predecessor=None):
        self.pos = pos
        self.distance = distance
        self.predecessor=predecessor

def get_distance(node:Node):
    return node.distance

def find_shortest_path(map:HighMap,start,stop):
    visited = set()
    graph = {}
    q = []
    n = Node(start,0)



    def move_direction(direction:Direction):
        new_pos = map.move_possible(n.pos,direction)
        distance = n.distance+1
        if new_pos != False and new_pos not in visited:
            node = Node(new_pos,distance,n)
            if new_pos in graph.keys():
                if distance < graph[new_pos].distance:
                    graph[new_pos] = node
            else:
                graph.update({new_pos:node})
                q.append(node)

            
    found = True

    while n.pos != stop:
        visited.add(n.pos)
        move_direction(LEFT)
        move_direction(RIGHT)
        move_direction(UP)
        move_direction(DOWN)
        if len(q)==0:
            found = False
            break
        q.sort(key=get_distance)
        n=q.pop(0)
    
    if not found:
        raise Exception("Dijkstra could not found path")
    
    return n.distance





        



            
    

with open(INPUT_FILE,"r") as lines:
    lines = [line.strip().replace("\n","") for line in lines]
    map = HighMap(lines)


start = map.start
end = map.end

solution = find_shortest_path(map,start,end)
    
print("Solution: " + str(solution))