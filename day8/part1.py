class Grid:
    
    def __init__(self):
        self._grid = []
    
    def addLine(self,line):
        self._grid.append(line)
    

    
    def isVisible(self,x,y):
        def get(x,y):
            return int(self._grid[y][x])
        
        def checkLine(stop):
            height_tree = get(x,y)
            for x_1 in range(x,stop[0],-1 if stop[0]<x else 1):
                h=get(x_1,y)
                if (x_1,y) != (x,y) and h>=height_tree:
                    return False
            
            for y_1 in range(y,stop[1],-1 if stop[1]<y else 1):
                h=get(x,y_1)
                if (x,y_1) != (x,y) and h >= height_tree:
                    return False
            
            return True
        
        height_tree = get(x,y)
        if self.isAtBorder(x,y) or checkLine((-1,y)) or checkLine((self.width,y)) or checkLine((x,-1)) or checkLine((x,self.height)):
            return True
        
        return False
        
        
        
    
    @property
    def width(self):
        return len(self._grid[0])
    
    @property 
    def height(self):
        return len(self._grid)
    
    def isAtBorder(self,x,y):
        pass
        return x==0 or y==0 or x==self.width-1 or y==self.height-1

grid = Grid()
with open("input.txt",'r',encoding = 'utf-8') as f:
    for line in f:
        line = line.strip().replace("\n","")
        grid.addLine(line)
  
  
solution = 0       

for x in range(grid.width):
    for y in range(grid.height):
        if grid.isVisible(x,y):
            solution = solution+1

print("Solution: " + str(solution))