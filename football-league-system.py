valid = False
while not valid:
    matches = int(input("How many matches has each team played: "))
    if matches >= 23:
        valid = True

clubs = ["" for _ in range(13)]
for i in range(13):
    print("Enter the name of team", i + 1, ":")
    clubs[i] = input()

stats = [[0 for _ in range(4)] for _ in range(13)]
highest = 0
points = [0 for _ in range(13)]

for i in range(13):
    valid = False
    while not valid:
        print("Enter statistics for team", clubs[i])
        won = int(input("Matches won: "))
        drawn = int(input("Matches drawn: "))
        lost = int(input("Matches lost: "))

        if won + drawn + lost != matches:
            print("Stats do not add up to matches played. Try again.")
        else:
            valid = True
            stats[i][1] = won
            stats[i][2] = lost
            stats[i][3] = drawn
            points[i] = won * 12 + drawn * 5
            stats[i][0] = points[i]
            if points[i] > highest:
                highest = points[i]

winners = []
for i in range(13):
    if points[i] == highest:
        winners.append(i)

print("The winner(s):")
for i in winners:
    print(clubs[i], "with points", highest, ",", stats[i][1], "wins and", stats[i][3], "draws")
