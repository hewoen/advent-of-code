import math
import time
from shutil import move
SQRT_2 = math.sqrt(2)


class Knot:
    def __init__(self):
        self._start = (-10,0)
        self._knots = [self._start for _ in range(10)]
        self._visited = {self._start}
    
    @property
    def tail(self):
        return self._knots[9]

    
  
    
    @property
    def head(self):
        return self._knots[0]

    @head.setter
    def head(self,v):
        self._knots[0]=v
    
    def isKnotAdjacent(self,knot_index):
        return math.sqrt(math.pow(self._knots[knot_index-1][0]-self._knots[knot_index][0],2)+math.pow(self._knots[knot_index-1][1]-self._knots[knot_index][1],2)) <= SQRT_2
        #return not(abs(self._knots[knot_index-1][0]-self._knots[knot_index][0])==2 or self._knots[knot_index-1][1]-self._knots[knot_index][1]==2)
        
    
    def moveTailTo(self,knot_index,pos):
        self._knots[knot_index]=pos
        if knot_index==9:
            self._visited.add(pos)

    
    def movementHead(self,direction,times):
        for i in range(times):
            match direction:
                case "L":
                    self.head = (self.head[0]-1,self.head[1])
                case "R":
                    self.head = (self.head[0]+1,self.head[1])
                case "U":
                    self.head = (self.head[0],self.head[1]-1)
                case "D":
                    self.head = (self.head[0],self.head[1]+1)
            
            #self.print()
            #time.sleep(1)

            for i in range(1,10):

                if not self.isKnotAdjacent(i):
                    dif = (self._knots[i-1][0]-self._knots[i][0],self._knots[i-1][1]-self._knots[i][1])
                    
                    a = abs(dif[0])+abs(dif[1])

                    # if dif==(2,2): #oben links
                    #     new_pos = (self._knots[i-1][0]-1,self._knots[i-1][1]-1)
                    # elif dif==(-2,2): #oben rechts
                    #     new_pos = (self._knots[i-1][0]+1,self._knots[i-1][1]-1)
                    # elif dif==(2,-2): #unten links
                    #     new_pos = (self._knots[i-1][0]-1,self._knots[i-1][1]+1)
                    # elif dif==(-2,2): #unten rechts
                    #     new_pos = (self._knots[i-1][0]+1,self._knots[i-1][1]-1)

                    if a==4:
                        norm = (int(dif[0]*(-1)/2),int(dif[1]*(-1)/2))
                        new_pos = (self._knots[i-1][0]+norm[0],self._knots[i-1][1]+norm[1])
                    elif dif[0]==-2:
                        new_pos = (self._knots[i-1][0]+1,self._knots[i-1][1])
                    elif dif[0]==2:
                        new_pos = (self._knots[i-1][0]-1,self._knots[i-1][1])
                    elif dif[1]==-2:
                        new_pos = (self._knots[i-1][0],self._knots[i-1][1]+1)
                    else:
                        new_pos = (self._knots[i-1][0],self._knots[i-1][1]-1)

                    self.moveTailTo(i,new_pos)
                    #self.print()
                    pass
            #self.print()
            pass
#            time.sleep(1)

        
    @property
    def movements(self):
        return len(self._visited)
    
    def print(self):
        for y in range(-20,20):
            line = ""
            for x in range(-20,20):
                c=False
                for i in range(0,10):
                    if (x,y) == self._knots[i]:
                        line = line + str(i)
                        c=True
                        break
                if c:
                    continue
                if False and (x,y)==self.head:
                    line = line + "h"
                elif True and (x,y) in self._visited:
                    line = line + "#"
                else:
                    line = line + "."
            print(line)
        


knot = Knot()
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        movement = line.split(" ")
        knot.movementHead(movement[0],int(movement[1]))

knot.print()        

solution = knot.movements

print(str(solution))