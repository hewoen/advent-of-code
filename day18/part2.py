import sys
sys.setrecursionlimit(1000000) 
INPUT = "input.txt"
#INPUT = "input_example.txt"
DROPLET=1
STEAM=2
AIR=3
solution=0
grid = {}
diffs = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,1),(0,0,-1)]
with open(INPUT) as f:
    lines = [f.strip().replace("\n","") for f in f.readlines()]




    
    
max_x = max([int(cords.split(",")[0]) for cords in lines])+3
max_y = max([int(cords.split(",")[1]) for cords in lines])+3
max_z = max([int(cords.split(",")[2]) for cords in lines])+3

for x in range(-2,max_x):
    for y in range(-2,max_y):
        for z in range(-2,max_z):
            grid[(x,y,z)] = AIR
            
for line in lines:
    cords = [int(x) for x in line.split(",")]
    grid[(cords[0],cords[1],cords[2])] = DROPLET

visited = []

def expand(x,y,z):
    if((x,y,z) in visited):
        return
    visited.append((x,y,z))
    for diff in diffs:
        x_1 = x+diff[0]
        y_1 = y+diff[1]
        z_1 = z+diff[2]
        chk = (x_1,y_1,z_1)
        keys = grid.keys()
        if(chk in keys and grid[chk]!=DROPLET):
            grid[chk] = STEAM
            expand(x_1,y_1,z_1)
            
expand(0,0,0)

            
for line in lines:
    cords = [int(x) for x in line.split(",")]
    for diff in diffs:
        x_1 = cords[0]+diff[0]
        y_1 = cords[1]+diff[1]
        z_1 = cords[2]+diff[2]
        chk = (x_1,y_1,z_1)
        keys = grid.keys()
        if(chk in keys and grid[chk]==STEAM):
            solution = solution+1

print("Solution: " + str(solution))