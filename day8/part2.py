class Grid:
    
    def __init__(self):
        self._grid = []
    
    def addLine(self,line):
        self._grid.append(line)
    

    
    def getScenic(self,x,y):
        def get(x,y):
            return int(self._grid[y][x])
        
        def lineValue(stop):
            height_tree = get(x,y)
            n=1
            if self.isAtBorder(x,y):
                return 0
            
            
            step=-1 if stop[0]<x else 1
            for x_1 in range(x+step,stop[0],step):
                h=get(x_1,y)
                if h>=height_tree or self.isAtBorder(x_1,y):
                    break
                n=n+1 
            
            step=-1 if stop[1]<y else 1
            for y_1 in range(y+step,stop[1],step):
                h=get(x,y_1)
                if h>=height_tree or self.isAtBorder(x,y_1):
                    break
                n=n+1
            
            
            return n
        
        return lineValue((-1,y))*lineValue((self.width,y))*lineValue((x,-1))*lineValue((x,self.height))
            
                
        
        
    
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
        scenic = grid.getScenic(x,y)
        if scenic>solution:
            solution=scenic

print("Solution: " + str(solution))