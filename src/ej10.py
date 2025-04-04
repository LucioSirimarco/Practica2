def charge_stats (stats):
    for player, player_stats in round.items():
        temp_points[player]= player_stats['kills'] * kill_value + player_stats['assists'] * assist_value + player_stats['deaths'] * death_value
        stats[player]['points'] += temp_points[player]
        for stat, stat_value in player_stats.items():
            if type(stat_value)==int:
                stats[player][stat]=stats[player][stat]+stat_value
            elif stat_value:
                stats[player][stat]=stats[player][stat]+1
    mvp = max(temp_points, key=temp_points.get)
    stats[mvp]['mvps'] += 1
    return stats
    

def print_rounds ():
    print("Jugador   |  Kills    |Asistencias|  Muertes  |    MVPs   |   Puntos")
    print("-"*80)
    sorted_stats = dict(sorted(stats.items(), key = lambda x: x[1].get('points'), reverse=True))
    for player, player_stats in sorted_stats.items():
        if(len(player) > 5):
            spaces = 4
        else:
            spaces = 5
        print(f'{player}{' '*spaces}|{' '*5}{player_stats['kills']}{' '*5}|{' '*5}{player_stats['assists']}{' '*5}|{' '*5}{player_stats['deaths']}{' '*5}|{' '*5}{player_stats['mvps']}{' '*5}|{' '*5}{player_stats['points']}')

rounds = [
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
}
]
kill_value = 3
assist_value = 1
death_value = -1
round_number = 1
temp_points = {
    'Shadow': 0,
    'Blaze': 0,
    'Viper': 0,
    'Frost': 0,
    'Reaper': 0, 
}
stats = {
'Shadow': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0},
'Blaze': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0},
'Viper': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0},
'Frost': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0},
'Reaper': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0}
}
if (len(rounds)>0):
    for round in rounds:
        charge_stats(stats)
        print("\n")
        print(f"Ranking ronda {round_number}:")
        round_number += 1
        print_rounds()
else: 
    print('No se jugaron rondas')