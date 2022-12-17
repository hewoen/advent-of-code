import json
def compare(left,right):
    
    
    if type(left)!=list:
        left=[left]
    if type(right)!=list:
        right=[right] 
    
    if left==right:
        return None
          
    
    for i in range(len(left)):
        if i>=len(right):
            return False
        elif (type(left[i])==list or type(right[i])==list):
            c = compare(left[i],right[i])
            if c is not None:
                return c
            else:
                continue
        elif left[i]<right[i]:
            return True
        elif left[i]>right[i]:
            return False
        
    return True

        
solution=0
signals = [[[2]],[[6]]]
with open("input.txt",'r',encoding = 'utf-8') as f:
    lines = [x.strip().replace("\n","") for x in f.readlines()]
    for i in range(0,len(lines),3):
        signals.append(json.loads(lines[i]))
        signals.append(json.loads(lines[i+1]))

sorted=False
while not sorted:
    sorted=True
    for i in range(len(signals)-1):
        c = compare(signals[i],signals[i+1])
        if not c:
            sorted=False
            signals[i],signals[i+1]=signals[i+1],signals[i]

solution = (signals.index([[2]])+1)*(signals.index([[6]])+1)

print(str(solution))