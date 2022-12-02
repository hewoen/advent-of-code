max = (0,1) #(currently max value, cnumber of elve)
elve_calories = 0
elve_count = 0

with open("input.txt",'r',encoding = 'utf-8') as f:
    for line in f:
        if line.strip() == "":
            print(elve_calories)
            elve_count = elve_count + 1
            if elve_calories > max[0]:
                max = (elve_calories,elve_count)
            elve_calories = 0
            
        else:
            elve_calories = elve_calories + int(line.strip())

print("solution:" + str(max[0]))
print("count: " + str(elve_count))