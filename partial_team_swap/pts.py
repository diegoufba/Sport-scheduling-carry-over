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
    
    for team in teams:

        team1 = schedule[team].index(t1)
        team2 = schedule[team].index(t2)
        schedule[team][team1],schedule[team][team2] = schedule[team][team2],schedule[team][team1]
    
    return schedule

def pts2(schedule,carry_over_table,weight_table,obj,r,t1,t2):

    new_obj = obj
    aux_carry_over_table = [x[:] for x in carry_over_table]
    aux_schedule = [x[:] for x in schedule]
    n_times = len(aux_schedule)

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
        time1 = aux_schedule[t1][r]
        time2 = aux_schedule[t2][r]

        if r == 0:
            time1e = aux_schedule[t1][-1]
            time2e = aux_schedule[t2][-1]
        else:
            time1e = aux_schedule[t1][r-1]
            time2e = aux_schedule[t2][r-1]

        if r == n_times-2:
            time1d = aux_schedule[t1][0]
            time2d = aux_schedule[t2][0]
        else:
            time1d = aux_schedule[t1][r+1]
            time2d = aux_schedule[t2][r+1]

        # Troca de times
        aux_schedule[t1][r] , aux_schedule[t2][r] = aux_schedule[t2][r],aux_schedule[t1][r]

        new_obj -= (
            (weight_table[time1e][time1] * aux_carry_over_table[time1e][time1]**2) + 
            (weight_table[time1][time1d] * aux_carry_over_table[time1][time1d]**2) + 
            (weight_table[time2e][time2] * aux_carry_over_table[time2e][time2]**2) +
            (weight_table[time2][time2d] * aux_carry_over_table[time2][time2d]**2) +

            (weight_table[time1e][time2] * aux_carry_over_table[time1e][time2]**2) + 
            (weight_table[time2][time1d] * aux_carry_over_table[time2][time1d]**2) + 
            (weight_table[time2e][time1] * aux_carry_over_table[time2e][time1]**2) +
            (weight_table[time1][time2d] * aux_carry_over_table[time1][time2d]**2)     
        )

        aux_carry_over_table[time1e][time1] -=1
        aux_carry_over_table[time1][time1d] -=1
        aux_carry_over_table[time2e][time2] -=1
        aux_carry_over_table[time2][time2d] -=1

        aux_carry_over_table[time1e][time2] +=1
        aux_carry_over_table[time2][time1d] +=1
        aux_carry_over_table[time2e][time1] +=1
        aux_carry_over_table[time1][time2d] +=1

        new_obj += (
            (weight_table[time1e][time1] * aux_carry_over_table[time1e][time1]**2) + 
            (weight_table[time1][time1d] * aux_carry_over_table[time1][time1d]**2) + 
            (weight_table[time2e][time2] * aux_carry_over_table[time2e][time2]**2) +
            (weight_table[time2][time2d] * aux_carry_over_table[time2][time2d]**2) +

            (weight_table[time1e][time2] * aux_carry_over_table[time1e][time2]**2) + 
            (weight_table[time2][time1d] * aux_carry_over_table[time2][time1d]**2) + 
            (weight_table[time2e][time1] * aux_carry_over_table[time2e][time1]**2) +
            (weight_table[time1][time2d] * aux_carry_over_table[time1][time2d]**2)     
        )

        teams.add(aux_schedule[t1][r])
        teams.add(aux_schedule[t2][r])
    
    for team in teams:

        team1 = aux_schedule[team].index(t1)
        team2 = aux_schedule[team].index(t2)

        time1 = aux_schedule[team][team1]
        time2 = aux_schedule[team][team2]

        if r == 0:
            time1e = aux_schedule[t1][-1]
            time2e = aux_schedule[t2][-1]
        else:
            time1e = aux_schedule[t1][r-1]
            time2e = aux_schedule[t2][r-1]

        if r == n_times-2:
            time1d = aux_schedule[t1][0]
            time2d = aux_schedule[t2][0]
        else:
            time1d = aux_schedule[t1][r+1]
            time2d = aux_schedule[t2][r+1]

        # Troca de times
        aux_schedule[t1][r] , aux_schedule[t2][r] = aux_schedule[t2][r],aux_schedule[t1][r]

        new_obj -= (
            (weight_table[time1e][time1] * aux_carry_over_table[time1e][time1]**2) + 
            (weight_table[time1][time1d] * aux_carry_over_table[time1][time1d]**2) + 
            (weight_table[time2e][time2] * aux_carry_over_table[time2e][time2]**2) +
            (weight_table[time2][time2d] * aux_carry_over_table[time2][time2d]**2) +

            (weight_table[time1e][time2] * aux_carry_over_table[time1e][time2]**2) + 
            (weight_table[time2][time1d] * aux_carry_over_table[time2][time1d]**2) + 
            (weight_table[time2e][time1] * aux_carry_over_table[time2e][time1]**2) +
            (weight_table[time1][time2d] * aux_carry_over_table[time1][time2d]**2)     
        )

        aux_carry_over_table[time1e][time1] -=1
        aux_carry_over_table[time1][time1d] -=1
        aux_carry_over_table[time2e][time2] -=1
        aux_carry_over_table[time2][time2d] -=1

        aux_carry_over_table[time1e][time2] +=1
        aux_carry_over_table[time2][time1d] +=1
        aux_carry_over_table[time2e][time1] +=1
        aux_carry_over_table[time1][time2d] +=1

        new_obj += (
            (weight_table[time1e][time1] * aux_carry_over_table[time1e][time1]**2) + 
            (weight_table[time1][time1d] * aux_carry_over_table[time1][time1d]**2) + 
            (weight_table[time2e][time2] * aux_carry_over_table[time2e][time2]**2) +
            (weight_table[time2][time2d] * aux_carry_over_table[time2][time2d]**2) +

            (weight_table[time1e][time2] * aux_carry_over_table[time1e][time2]**2) + 
            (weight_table[time2][time1d] * aux_carry_over_table[time2][time1d]**2) + 
            (weight_table[time2e][time1] * aux_carry_over_table[time2e][time1]**2) +
            (weight_table[time1][time2d] * aux_carry_over_table[time1][time2d]**2)     
        )


        aux_schedule[team][team1],aux_schedule[team][team2] = aux_schedule[team][team2],aux_schedule[team][team1]
    
    return new_obj,aux_schedule
