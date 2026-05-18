team = {}
for i in range(11):
    name = input("Enter player name: ")
    height = float(input("Enter height: "))
    team[name] = height

captain = max(team, key=team.get)

print("Captain is:", captain)
print("Height:", team[captain])