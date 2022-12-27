l=["A","B","C","D","E"]
l="DCEBHJ"
l2=l

for a in l:
    l2 = [e for e in l2 if e!=a]
    for b in l2:
        print(a+b)

not_in = []
for x in l:
    for i in range(1):
        