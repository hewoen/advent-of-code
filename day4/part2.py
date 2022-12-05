def getAssingments(section):
    s = [int(x) for x in section.split("-")]
    return [x for x in range(s[0],s[1]+1)]

def doesOverlap(a,b):
    for x in a:
        if x in b:
            return True
    return False
    

with open("input.txt",'r',encoding = 'utf-8') as f:
   containing_assignemnts = 0
   for line in f:
       elves = [x.strip() for x in line.split(",")]
       a,b = getAssingments(elves[0]),getAssingments(elves[1])
       if doesOverlap(a,b):
           containing_assignemnts = containing_assignemnts+1
    
print("Solution: " + str(containing_assignemnts))