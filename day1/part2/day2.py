elves = []
elve_calories = 0


with open("input.txt",'r',encoding = 'utf-8') as f:
    for line in f:
        if line.strip() == "":
            print(elve_calories)
            elves.append(elve_calories)
            elve_calories=0
            
        else:
            elve_calories = elve_calories + int(line.strip())

sum=0
elves.sort(reverse=True)
for i in range(3):
    sum = sum+elves[i]
print("solution: " + str(sum))