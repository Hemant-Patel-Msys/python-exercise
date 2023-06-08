def calculate_points(*teams):
    t = []
    for team in teams:
        t.append(team[0]*3 + team[1]*1 + team[2]*(-1))
    sum = max(t)
    index = t.index(sum)
    return f"Winner: Team{index+1}"

Team1 = (3,4,2)
Team2 = (5,0,2)
Team3 = (0,0,1)

f = calculate_points(Team1,Team2,Team3)
print(f)

