
def score_round(opponent, me):
	#A: Rock
	#B: Paper
	#C: Scissor

	points = {"A":1,"B":2,"C":3}
	
	score = 0

	if me == "X":
		score =  points["A"] if opponent=="B" else points["B"] if opponent=="C" else points["C"]
	elif me == "Y":
		score = 3 + points[opponent]
	elif me == "Z":
		score = 6 + (points["B"] if opponent=="A" else points["C"] if opponent=="B" else points["A"])

	return score

total_score = 0

with open("input.txt",'r',encoding = 'utf-8') as f:
	for line in f:
		round = line.strip().split(" ")
		total_score = total_score + score_round(round[0],round[1])
     
print("Solution: " + str(total_score))