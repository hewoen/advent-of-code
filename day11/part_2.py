import time


def get_value_for_operation(v,old):
    if v.strip()=="old":
        return old
    else:
        return int(v)
        

class Item:
    def __init__(self,worry_level) -> None:
        self._init_worry_level = worry_level
        self._worry_level = {}
    
    def calm_down(self):
        pass
        #self._worry_level=int(self._worry_level/3)
    
    def get_worry_level(self,monkey_index):
        if monkey_index not in self._worry_level.keys():
            return self._init_worry_level
        else:
            return self._worry_level[monkey_index]
    
    def set_worry_level(self,monkey_index,worry_level):
        self._worry_level.update({monkey_index:worry_level})


class Monkey:
    def __init__(self,starting_items,operation,test) -> None:
        self._items = starting_items
        self._operation = operation
        self._test = test
        self._inspecting_count = 0
    

            
    def do_test(self,item,monkey_index):
        return self._test[1] if item.get_worry_level(monkey_index) % self._test[0]==0 else self._test[2]
    
    def do_operation(self,item,monkeys):
        for i,monky in enumerate(monkeys):
            worry_level = int(item.get_worry_level(i))
            if "+" in self._operation:
                values = self._operation.split("+")
                worry_level = get_value_for_operation(values[0],worry_level) + get_value_for_operation(values[1],worry_level)
            else:
                values = self._operation.split("*")
                worry_level = get_value_for_operation(values[0],worry_level) * get_value_for_operation(values[1],worry_level)
            item.set_worry_level(i,worry_level%monky._test[0])
        
    
    def turn(self,monkeys,i):
           
        while len(self._items) > 0:
           item = self._items[0]
           self._inspecting_count = self._inspecting_count+1
           self.do_operation(item,monkeys)
           decision_next_monkey = self.do_test(item,i)
           self.throwItem(0,monkeys[decision_next_monkey])
    
    def catchObject(self,item):
        self._items.append(item)
    
    def throwItem(self,item_index,to):
        to.catchObject(self._items.pop(item_index))
        
    @property
    def inspectingCount(self):
        return self._inspecting_count
     

    
    

def play_round(monkeys):
    for i,monkey in enumerate(monkeys):
        monkey.turn(monkeys,i)
    
monkeys = []
ROUNDS = 10000


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
print("execution time: " + str(time.process_time()))