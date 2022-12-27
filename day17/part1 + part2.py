N=0
M=1
R=2

margin_bottom = 3
tall = 0
WIDTH = 7

chamber = []

            


class Form:
    def __init__(self,width,height,offset=2) -> None:
        self._width=width
        self._tall=height
        self._positions = []
        self._offset = offset
        
    def add_position(self,x,y):
        self._positions.append((self._offset+x,y+tall+margin_bottom+1))
    
    def push(self,direction):
        d = 1 if direction==">" else -1
        for (x,y) in self._positions:
            if x+d < 0 or x+d >= WIDTH or (x+d,y) in chamber:
                return 

        for i in range(len(self._positions)):
            self._positions[i] = (self._positions[i][0]+d,self._positions[i][1])
    
    def fall_down(self):
        for (x,y) in self._positions:
            if y-1==0 or (x,y-1) in chamber:
                return False
        
        for i in range(len(self._positions)):
                x,y = self._positions[i]
                self._positions[i] = (x,y-1)
        
        return True
    
    
    @property 
    def top(self):
        top=self._positions[0]
        for position in self._positions:
            if position[1]>top[1]:
                top = position
        
        return top
    
    @property
    def positions(self):
        return self._positions
        
class _(Form):
    def __init__(self,offset=2) -> None:
        super().__init__(4,1,offset)
        self.add_position(0,0)
        self.add_position(1,0)
        self.add_position(2,0)
        self.add_position(3,0)

class Plus(Form):
    def __init__(self,offset=2) -> None:
        super().__init__(3,3,offset)
        self.add_position(1,2)
        self.add_position(0,1)
        self.add_position(1,1)
        self.add_position(2,1)
        self.add_position(1,0)
        
class L(Form):
    def __init__(self, offset=2) -> None:
        super().__init__(3, 3, offset)
        self.add_position(2,2)
        self.add_position(2,1)
        self.add_position(0,0)
        self.add_position(1,0)
        self.add_position(2,0)

class I(Form):
    def __init__(self, offset=2) -> None:
        super().__init__(1, 4, offset)
        self.add_position(0,3)
        self.add_position(0,2)
        self.add_position(0,1)
        self.add_position(0,0)

class Square(Form):
    def __init__(self, offset=2) -> None:
        super().__init__(2, 2, offset)
        self.add_position(0,1)
        self.add_position(1,1)
        self.add_position(0,0)
        self.add_position(1,0)



def create_form(i)->Form:
    if i==0:
        return _()
    elif i==1:
        return Plus()
    elif i==2:
        return L()
    elif i==3:
        return I()
    elif i==4:
        return Square()

 

top=(0,3)
        
INPUT = "input.txt"
#INPUT = "input_example.txt"
    
with open(INPUT) as f:
    for line in f:
        directions = line.strip().replace("\n","")


CYCLES = 2022
#CYCLES = 1000000000000


def p(l=[]):
    t=chamber + l
    for y in range(tall,0,-1):
        s=""
        for x in range(7):
            if (x,y) in t:
                s=s+"#"
            else:
                s=s+"."

        print(s)
    print(" ")
    
def simulate(cycles):
    global chamber,tall
    chamber.clear()
    tall = 0
    t=0
    ii=0
    count_directions = len(directions)
    count=0
    for i in range(cycles):
        form = create_form(i%5)
        in_movement=True
        while in_movement:
            form.push(directions[count])
            count=(count+1)%count_directions
            in_movement=form.fall_down()
            #tall = max(tall,form.top[1])
            #p(form.positions)
            if count==0:
                print(str(i-ii) + ": " + str(tall-t))
                ii=i
                t=tall
            pass
        chamber = chamber + form.positions
        tall = max(tall,form.top[1])
        #p()
        pass
    return tall
    
if CYCLES<=2*1745-1:
    solution = simulate(CYCLES)
else:
    cycles_to_simulate = 1744 + (CYCLES-1744)%1745
    repeats = int((CYCLES-1744)/1745)
    solution = simulate(cycles_to_simulate) + repeats*2778

print("Solution: " + str(solution))