def pts(schedule,r,t1,t2):

    # schedule = [
    #     [3,7,5,1,2,4,6],
    #     [5,4,3,0,7,6,2],
    #     [4,3,6,5,0,7,1],
    #     [0,2,1,7,6,5,4],
    #     [2,1,7,6,5,0,3],
    #     [1,6,0,2,4,3,7],
    #     [7,5,2,4,3,1,0],
    #     [6,0,4,3,1,2,5],
    # ]

    initial_round = r
    rounds = [r]
    teams = set()
    for i in range (len(schedule)-1):
        next_r = schedule[t1].index(schedule[t2][r])

        if next_r == initial_round:
            break
        else:
            r = next_r
            rounds.append(r)
    
    for r in rounds:
        # Troca de times
        aux = schedule[t1][r]
        schedule[t1][r] = schedule[t2][r]
        schedule[t2][r] = aux
        
        teams.add(schedule[t1][r])
        teams.add(schedule[t2][r])
    
    # for team in teams:

    #     team1 = schedule[team].index(t1)
    #     team2 = schedule[team].index(t2)
    #     schedule[team][team1],schedule[team][team2] = schedule[team][team2],schedule[team][team1]
    
    return schedule
