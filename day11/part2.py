class Item:
    def __init__(self,worry_level) -> None:
        self._worry_level = worry_level
    
    def calm_down(self):
        self._worry_level=int(self._worry_level/3)
    
    @property
    def worry_level(self):
        return self._worry_level
    
    @worry_level.setter
    def worry_level(self,worry_level):
        self._worry_level = worry_level

class Monkey:
    def __init__(self,starting_items,operation,test) -> None:
        self._items = starting_items
        self._operation = operation
        self._test = test
        self._inspecting_count = 0
    
    def do_operation(self,item):
        if "+" in self._operation:
            values = self._operation.split("+")
            item.worry_level = get_value_for_operation(values[0],item.worry_level) + get_value_for_operation(values[1],item.worry_level)
        else:
            values = self._operation.split("*")
            item.worry_level = get_value_for_operation(values[0],item.worry_level) * get_value_for_operation(values[1],item.worry_level)
            
    def do_test(self,item):
        return self._test[1] if item.worry_level%self._test[0]==0 else self._test[2]
    
    def turn(self,monkeys):
           
        while len(self._items) > 0:
           item = self._items[0]
           self._inspecting_count = self._inspecting_count+1
           self.do_operation(item)
           item.calm_down()
           decision_next_monkey = self.do_test(item)
           self.throwItem(0,monkeys[decision_next_monkey])
    
    def catchObject(self,worry_level):
        self._items.append(worry_level)
    
    def throwItem(self,item_index,to):
        to.catchObject(self._items.pop(item_index))
        
    @property
    def inspectingCount(self):
        return self._inspecting_count
     
def get_value_for_operation(v,old):
    if v.strip()=="old":
        return old
    else:
        return int(v)
    
    

def play_round(monkeys):
    for monkey in monkeys:
        monkey.turn(monkeys)
    
monkeys = []
ROUNDS = 10


with open("input.txt",'r',encoding = 'utf-8') as f:
    lines = [x.strip().replace("\n","") for x in f.readlines()]
    for i in range(0,len(lines),7):
        starting_items =[Item(int(x)) for x in lines[i+1][16::].split(",")]
        operation = lines[i+2][17::]

        
        s = lines[i+3].split("by")
        divisor = int(s[1])
        s_1 = int(lines[i+4].split("monkey")[1])
        s_2 = int(lines[i+5].split("monkey")[1])
        test=(divisor,s_1,s_2)
        
        monkeys.append(Monkey(starting_items,operation,test))
        

        

for i in range(ROUNDS):
    play_round(monkeys)
    pass

inspecting_counts = [x.inspectingCount for x in monkeys]     
inspecting_counts.sort(reverse=True)      
  
     
solution = inspecting_counts[0]*inspecting_counts[1]
print("Solution: " + str(solution))