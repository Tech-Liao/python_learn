import sys


def compute(data):
    team_scores = {"A": {"win": 0, "draw": 0, "loss": 0, "goal": 0},
                   "B": {"win": 0, "draw": 0, "loss": 0, "goal": 0},
                   "C": {"win": 0, "draw": 0, "loss": 0, "goal": 0},
                   "D": {"win": 0, "draw": 0, "loss": 0, "goal": 0},
                   "E": {"win": 0, "draw": 0, "loss": 0, "goal": 0},
                   "F": {"win": 0, "draw": 0, "loss": 0, "goal": 0}}
    for i in range(15):
        teamA = data[i][0]
        teamB = data[i][1]
        result1 = [int(data[i][2]), int(data[i][3])]
        result2 = [int(data[i][4]), int(data[i][5])]
        team_scores[teamA]["goal"] += (result1[0] + result2[0])
        team_scores[teamB]["goal"] += (result1[1] + result2[1])
        team_scores[teamA]["loss"] -= (result1[1] + result2[1])
        team_scores[teamB]["goal"] += (result1[0] + result2[0])
        if result1[0] > result1[1]:
            team_scores[teamA]["win"] += 3
        elif result1[0] < result1[1]:
            team_scores[teamB]["win"] += 3
        else:
            team_scores[teamB]["win"] += 1
            team_scores[teamA]["win"] += 1
    return team_scores


count = 0
data = []
for line in sys.stdin:
    temp = line.split()
    if len(temp) == 1:
        count = int(temp[0])
        continue
    data.append(temp)

for i in range(count):
    result = compute(data[i * 15:(i + 1) * 15])
    for key in result.keys():
        print("{} {} {}".format(result[key]["win"],result[key]["goal"]-result[key]["loss"],result[key]["goal"]))

