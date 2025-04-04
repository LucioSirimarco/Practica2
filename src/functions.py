def charge_stats (stats,round, kill_value, assist_value, death_value):
    temp_points = {player: 0 for player in stats}
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
    

def print_rounds (stats):
    print("Jugador   |  Kills    |Asistencias|  Muertes  |    MVPs   |   Puntos")
    print("-"*80)
    sorted_stats = dict(sorted(stats.items(), key = lambda x: x[1].get('points'), reverse=True))
    for player, player_stats in sorted_stats.items():
        if(len(player) > 5):
            spaces = 4
        else:
            spaces = 5
        print(f'{player}{' '*spaces}|{' '*5}{player_stats['kills']}{' '*5}|{' '*5}{player_stats['assists']}{' '*5}|{' '*5}{player_stats['deaths']}{' '*5}|{' '*5}{player_stats['mvps']}{' '*5}|{' '*5}{player_stats['points']}')