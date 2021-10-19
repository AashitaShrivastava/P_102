import random
player=["Ananya","Avani","Aarya","Siya"]
number_of_participants=len(player)
teams=2

while number_of_participants>0 and teams>0:
    team=random.sample(player,int(number_of_participants/teams))
    for x in team:
        player.remove(x)
        number_of_participants-=int(number_of_participants/teams)
        teams-=1
print(team)