def hasMarker(str):
    chars = []
    for c in str:
        if c in chars:
            return False
        chars.append(c)
    return True
        
with open("input.txt",'r',encoding = 'utf-8') as f:
    line = f.readline().strip()
    for i in range(14,len(line)+1,1):
        if(hasMarker(line[i-14:i])):
            solution = str(i)
            break
    
                


print("Solution: " + solution)