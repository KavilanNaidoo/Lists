#Kavilan Naidoo
#13-01-2015
#2d list function

players = [
    ["k1llmAchine",51,49],
    ["Bob2247",15,99],
    ["hAxOr12",40,12]
]
print("-"*21)
for player in players:
    print("|{0:<11}|{1:<3}|{2:<3}|".format(player[0],player[1],player[2]))
    print("-"*21)
