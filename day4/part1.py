def getAssingments(section):
    s = [int(x) for x in section.split("-")]
    return [x for x in range(s[0],s[1]+1)]

def doesFullyContain(a,b):
    for x in a:
        if x not in b:
            return False
    return True
    

with open("input.txt",'r',encoding = 'utf-8') as f:
   containing_assignemnts = 0
   for line in f:
       elves = [x.strip() for x in line.split(",")]
       a,b = getAssingments(elves[0]),getAssingments(elves[1])
       if doesFullyContain(a,b) or doesFullyContain(b,a):
           containing_assignemnts = containing_assignemnts+1
    
print("Solution: " + str(containing_assignemnts))