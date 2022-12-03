
def score_round(opponent, me):
	#A: Rock
	#B: Paper
	#C: Scissor

	replacements = [("X","A"),("Y","B"),("Z","C")]


	for replacement in replacements:
		me = me.replace(replacement[0],replacement[1])

	score = 0

	if me == "A":
		score =  1
	elif me == "B":
		score = 2
	elif me == "C":
		score = 3

	if opponent==me:
		return score+3

	if me=="A" and opponent=="C" or me=="C" and opponent=="B" or me=="B" and opponent=="A":
		return score+6

	return score

total_score = 0

with open("input.txt",'r',encoding = 'utf-8') as f:
	for line in f:
		round = line.strip().split(" ")
		total_score = total_score + score_round(round[0],round[1])
     
print("Solution: " + str(total_score))