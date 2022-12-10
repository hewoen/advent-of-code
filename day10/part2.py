class Instruction:
    def __init__(self,cycles) -> None:
        self._remainig_cycles=cycles
        self._register=None
    
    def setRegister(self,register):
        self._register=register
        
    def executeTask(self):
        pass    
    
    def tick(self):
        self._remainig_cycles=self._remainig_cycles-1
        self.executeTask()
        return self.finished
        
    @property
    def finished(self):
        return self._remainig_cycles <= 0    

class ADDX(Instruction):
    def __init__(self,V) -> None:
        super().__init__(2)
        self._V = V
    
    def executeTask(self):
        if self.finished:
            self._register["X"]=self._register["X"]+self._V
            pass
    
class NOOP(Instruction):
    def __init__(self) -> None:
        super().__init__(1)
        

class CPU:
    def __init__(self) -> None:
        self._register = {"X":1}
        self._cycle = 1
    
    def setInstruction(self, instruction:Instruction):
        instruction.setRegister(self._register)
        self._instruction = instruction
    
    def tick(self):
        self._cycle = self._cycle+1
        return self._instruction.tick()
    
    def getRegister(self,r):
        return self._register[r]
    
    @property
    def cycle(self):
        return self._cycle
        
        
        
solution=""
cpu = CPU()

def isSpiteAtPos(pos,pos_middle_spite):
    pos = pos%40
    return pos>=pos_middle_spite-1 and pos <=pos_middle_spite+1

with open("input.txt",'r',encoding = 'utf-8') as f:
    for line in f:
        line = line.strip().replace("\n","")
        if line=="noop":
            instruction = NOOP()
        else:
            s = line.split(" ")
            V = int(s[1])
            instruction = ADDX(V)
        
        cpu.setInstruction(instruction)
        
        while not instruction.finished:
            spite_middle = cpu.getRegister("X")
            solution = solution + ("#" if isSpiteAtPos(len(solution),spite_middle) else ".")
            cpu.tick()


for i in range(0,240,40):
    print(solution[i:i+41])