import re

class Stack:
    def __init__(self):
        self._stack = []
    def push(self,obj):
        self._stack.append(obj)
    def push_1(self,obj):
        self._stack = [obj] + self._stack
        
    def pop(self):
        return self._stack.pop(-1)

class Stacks:
    def __init__(self):
        self._stacks=[]
    
    def length(self):
        return len(self._stacks)
    
    def add(self,i_stack,obj):
        while(len(self._stacks)-1 < i_stack):
            self._stacks.append(Stack())
        self._stacks[i_stack].push_1(obj)
    def get(self,i_stack)->Stack:
        return self._stacks[i_stack]
        

stacks = Stacks()
pattern = re.compile(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)")
with open("input.txt",'r',encoding = 'utf-8') as f:
    for line in f:
        line=line.replace("\n","")
        if line!="" and line[0:4] != "move":
            i=1
            while i<len(line):
                if(line[i]!=" " and not line[i].isdigit()):
                    stacks.add(int((i-1)/4),line[i])
                i=i+4
        elif line[0:4] == "move":
            cmd = pattern.match(line)
            #print(int(stacks.length()))
            print("move " + cmd.group(1) + " from " + cmd.group(2) + " to " + cmd.group(3))
            for i in range(int(cmd.group(1))):
                stacks.get(int(cmd.group(3))-1).push(stacks.get(int(cmd.group(2))-1).pop())
                

solution = ""

for i in range(stacks.length()):
    solution = solution + stacks.get(i).pop().replace("[","").replace("]","")

print("Solution: " + solution)