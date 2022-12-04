def getCompartments(rucksack):
    rucksack=rucksack.strip()
    length = len(rucksack)
    return (rucksack[0:int(length/2)],rucksack[int(length/2):])


def getItemValue(item):
    if item.isupper():
        return ord(item)-38
    else:
        return ord(item)-96
    
def sameItemInRucksacks(rucksacks):
    max_index = 0
    max_length = len(rucksacks[0])
    for i in range(len(rucksacks)):
        if len(rucksacks[i])>max_length:
            max_length = len(rucksacks[i])
            max_index = i
            
    for item in rucksacks[max_index]:
        in_all = True
        for i in range(len(rucksacks)):
            if i==max_index:
                continue
            elif item not in rucksacks[i]:
                in_all = False
                continue
        if in_all:
            return item
    
        
        


with open("input.txt",'r',encoding = 'utf-8') as f:
    total_priorities = 0
    lines = f.readlines()
    for i in range(0,len(lines),3):
        print(lines[i:i+3])
        same_item = sameItemInRucksacks(lines[i:i+3])
        print(same_item)
        total_priorities = total_priorities + getItemValue(same_item)
        
    
print("Solution:" + str(total_priorities))