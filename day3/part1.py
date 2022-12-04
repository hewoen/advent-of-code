def getCompartments(rucksack):
    rucksack=rucksack.strip()
    length = len(rucksack)
    return (rucksack[0:int(length/2)],rucksack[int(length/2):])


def getItemValue(item):
    if item.isupper():
        return ord(item)-38
    else:
        return ord(item)-96
    
def sameItemInBothCompartments(compartments):
    for item in compartments[0]:
        if item in compartments[1]:
            return item


with open("input.txt",'r',encoding = 'utf-8') as f:
    total_priorities = 0
    for line in f:
        compartments = getCompartments(line)
        print(compartments)
        same_item = sameItemInBothCompartments(compartments)
        total_priorities = total_priorities + getItemValue(same_item)
    
print("Solution:" + str(total_priorities))