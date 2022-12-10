import math
from shutil import move
SQRT_2 = math.sqrt(2)


class Knot:
    def __init__(self):
        self._start = (0,0)
        self._pos_head = self._start
        self._pos_tail = self._start
        self._visited = {self._pos_tail}
    
    def isTailAdjacent(self):
        return math.sqrt(math.pow(self._pos_head[0]-self._pos_tail[0],2)+math.pow(self._pos_head[1]-self._pos_tail[1],2)) <= SQRT_2
    
    def moveTailTo(self,pos):
        self._pos_tail=pos
        self._visited.add(pos)

    
    def movementHead(self,direction,times):
        for i in range(times):
            match direction:
                case "L":
                    self._pos_head = (self._pos_head[0]-1,self._pos_head[1])
                case "R":
                    self._pos_head = (self._pos_head[0]+1,self._pos_head[1])
                case "U":
                    self._pos_head = (self._pos_head[0],self._pos_head[1]-1)
                case "D":
                    self._pos_head = (self._pos_head[0],self._pos_head[1]+1)

            if not self.isTailAdjacent():
                dif = (self._pos_head[0]-self._pos_tail[0],self._pos_head[1]-self._pos_tail[1])

                if dif[0]==-2:
                    new_pos = (self._pos_head[0]+1,self._pos_head[1])
                elif dif[0]==2:
                    new_pos = (self._pos_head[0]-1,self._pos_head[1])
                elif dif[1]==-2:
                    new_pos = (self._pos_head[0],self._pos_head[1]+1)
                else:
                    new_pos = (self._pos_head[0],self._pos_head[1]-1)

                self.moveTailTo(new_pos)
    
    @property
    def movements(self):
        return len(self._visited)


knot = Knot()
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        movement = line.split(" ")
        knot.movementHead(movement[0],int(movement[1]))


solution = knot.movements

print(str(solution))