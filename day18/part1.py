      
#INPUT = "input.txt"
INPUT = "input_example.txt"

solution=0
    
with open(INPUT) as f:
    lines = [f.strip().replace("\n","") for f in f.readlines()]

def check_cords(x,y,z):
    s=str(x)+","+str(y)+","+str(z)
    return s in lines

diffs = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,1),(0,0,-1)]

for line in lines:
    (x,y,z) = [int(x) for x in line.split(",")]
    for diff in diffs:
        if not check_cords(x+diff[0],y+diff[1],z+diff[2]):
            solution=solution+1
        
        



print("Solution: " + str(solution))