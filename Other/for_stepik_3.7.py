n = int(input())
team_list = []


def index_of_team_in_list(team):
    if len(team_list) == 0:
        return -1
    for item in team_list:
        if item[0] == team:
            return team_list.index(item)
    return -1


for _ in range(n):
    temp = input().split(';')
    ind1, ind2 = index_of_team_in_list(temp[0]), index_of_team_in_list(temp[2])
    if ind1 == -1:
        team_list.append([temp[0], 0, 0, 0, 0, 0])
    if ind2 == -1:
        team_list.append([temp[2], 0, 0, 0, 0, 0])
    ind1, ind2 = index_of_team_in_list(temp[0]), index_of_team_in_list(temp[2])
    team_list[ind1][1] += 1
    team_list[ind2][1] += 1
    if int(temp[1]) > int(temp[3]):
        team_list[ind1][2] += 1
        team_list[ind2][4] += 1
        team_list[ind1][5] += 3
    elif int(temp[1]) < int(temp[3]):
        team_list[ind1][4] += 1
        team_list[ind2][2] += 1
        team_list[ind2][5] += 3

    else:
        team_list[ind1][3] += 1
        team_list[ind2][3] += 1
        team_list[ind1][5] += 1
        team_list[ind2][5] += 1

for item in team_list:
    print(f'{item[0]}: {item[1]} {item[2]} {item[3]} {item[4]} {item[5]}')
