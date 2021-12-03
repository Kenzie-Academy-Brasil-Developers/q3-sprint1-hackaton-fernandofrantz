# Seu código aqui
hackathon_1 = ["Team Kenzie", "Team Ateliware", "Team VHSYS", "Team Mirum"]
hackathon_2 = ["Team Ateliware", "Team Kenzie", "Team VHSYS", "Team Mirum"]
hackathon_3 = ["Team Mirum", "Team Ateliware","Team VHSYS", "Team Kenzie"]

def get_score(team_name, teams):
    position = 1
    for place in teams:
        if place != team_name:
            position += 1
        elif place == team_name:
            position = position
            break
    print(f'A {team_name} ficou classificada em {position}º lugar')
    return f'A {team_name} ficou classificada em {position}º lugar'

print(' => Team Kenzie deve finalizar em 1º lugar:')
get_score('Team Kenzie', hackathon_1)
print('- - ' *15)
print('')


print(' => Team Kenzie deve finalizar em 2º lugar:')
get_score('Team Kenzie', hackathon_2)
print('- - ' *15)
print('')

print(' => Team Kenzie deve finalizar em 4º lugar:')
get_score('Team Kenzie', hackathon_3)
print('- - ' *15)
print('')
