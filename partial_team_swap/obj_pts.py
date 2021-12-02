from objetivo import objetivo
from partial_team_swap.pts import pts

import more_itertools as mit

def obj_pts(obj,schedule,r,t1,t2,weight_table,carry_over_table):    

    new_obj = obj
    aux_carry_over_table = [x[:] for x in carry_over_table]
    aux_schedule = [x[:] for x in schedule]
    n_times = len(aux_schedule)

    initial_round = r
    rounds = [r]
    for i in range (len(aux_schedule)-1):
        next_r = aux_schedule[t1].index(aux_schedule[t2][r])

        if next_r == initial_round:
            break
        else:
            r = next_r
            rounds.append(r)   

    rounds.sort()
    #print(rounds)

    times_consecutivos = [list(x) for x in mit.consecutive_groups(rounds)]
    if times_consecutivos[0][0] == 0 and times_consecutivos[-1][-1] == n_times-2:
        times_consecutivos[-1] += times_consecutivos[0]
        times_consecutivos.pop(0)
    #print(times_consecutivos)

    for r in rounds:
        l1,l2 = [i for i in range(n_times) if aux_schedule[i][r] == t1 or aux_schedule[i][r] == t2]
        t11 = aux_schedule[l1][r]
        t21 = aux_schedule[l2][r]
        
        if r == 0:
            t11e = aux_schedule[l1][-1]
            t21e = aux_schedule[l2][-1]

        else:
            t11e = aux_schedule[l1][r-1]
            t21e = aux_schedule[l2][r-1]

        if r == n_times-2:

            t11d = aux_schedule[l1][0]
            t21d = aux_schedule[l2][0]   
        else:

            t11d = aux_schedule[l1][r+1]
            t21d = aux_schedule[l2][r+1]

        new_obj -= (
            (weight_table[t11e][t11] * aux_carry_over_table[t11e][t11]**2) + 
            (weight_table[t21e][t21] * aux_carry_over_table[t21e][t21]**2) + 
            (weight_table[t11][t11d] * aux_carry_over_table[t11][t11d]**2) +
            (weight_table[t21][t21d] * aux_carry_over_table[t21][t21d]**2) +

            (weight_table[t11e][t21] * aux_carry_over_table[t11e][t21]**2) + 
            (weight_table[t21e][t11] * aux_carry_over_table[t21e][t11]**2) + 
            (weight_table[t21][t11d] * aux_carry_over_table[t21][t11d]**2) +
            (weight_table[t11][t21d] * aux_carry_over_table[t11][t21d]**2)     
        )

        aux_carry_over_table[t11e][t11] -=1
        aux_carry_over_table[t21e][t21] -=1
        aux_carry_over_table[t11][t11d] -=1
        aux_carry_over_table[t21][t21d] -=1

        aux_carry_over_table[t11e][t21] +=1
        aux_carry_over_table[t21e][t11] +=1
        aux_carry_over_table[t21][t11d] +=1
        aux_carry_over_table[t11][t21d] +=1       

        new_obj += (
            (weight_table[t11e][t11] * aux_carry_over_table[t11e][t11]**2) + 
            (weight_table[t21e][t21] * aux_carry_over_table[t21e][t21]**2) + 
            (weight_table[t11][t11d] * aux_carry_over_table[t11][t11d]**2) +
            (weight_table[t21][t21d] * aux_carry_over_table[t21][t21d]**2) +

            (weight_table[t11e][t21] * aux_carry_over_table[t11e][t21]**2) + 
            (weight_table[t21e][t11] * aux_carry_over_table[t21e][t11]**2) + 
            (weight_table[t21][t11d] * aux_carry_over_table[t21][t11d]**2) +
            (weight_table[t11][t21d] * aux_carry_over_table[t11][t21d]**2)     
        )

        aux_schedule[l1][r],aux_schedule[l2][r] = aux_schedule[l2][r],aux_schedule[l1][r]

    for times in times_consecutivos:
        if len(times) == 1:
            r01 = times[0]

            t11 = aux_schedule[t1][r01]
            t21 = aux_schedule[t2][r01]
            
            if r01 == 0:
                t11e = aux_schedule[t1][-1]
                t21e = aux_schedule[t2][-1]

            else:
                t11e = aux_schedule[t1][r01-1]
                t21e = aux_schedule[t2][r01-1]

            if r01 == n_times-2:

                t11d = aux_schedule[t1][0]
                t21d = aux_schedule[t2][0]   
            else:

                t11d = aux_schedule[t1][r01+1]
                t21d = aux_schedule[t2][r01+1]

            new_obj -= (
                (weight_table[t11e][t11] * aux_carry_over_table[t11e][t11]**2) + 
                (weight_table[t21e][t21] * aux_carry_over_table[t21e][t21]**2) + 
                (weight_table[t11][t11d] * aux_carry_over_table[t11][t11d]**2) +
                (weight_table[t21][t21d] * aux_carry_over_table[t21][t21d]**2) +

                (weight_table[t11e][t21] * aux_carry_over_table[t11e][t21]**2) + 
                (weight_table[t21e][t11] * aux_carry_over_table[t21e][t11]**2) + 
                (weight_table[t21][t11d] * aux_carry_over_table[t21][t11d]**2) +
                (weight_table[t11][t21d] * aux_carry_over_table[t11][t21d]**2)     
            )

            aux_carry_over_table[t11e][t11] -=1
            aux_carry_over_table[t21e][t21] -=1
            aux_carry_over_table[t11][t11d] -=1
            aux_carry_over_table[t21][t21d] -=1

            aux_carry_over_table[t11e][t21] +=1
            aux_carry_over_table[t21e][t11] +=1
            aux_carry_over_table[t21][t11d] +=1
            aux_carry_over_table[t11][t21d] +=1       

            new_obj += (
                (weight_table[t11e][t11] * aux_carry_over_table[t11e][t11]**2) + 
                (weight_table[t21e][t21] * aux_carry_over_table[t21e][t21]**2) + 
                (weight_table[t11][t11d] * aux_carry_over_table[t11][t11d]**2) +
                (weight_table[t21][t21d] * aux_carry_over_table[t21][t21d]**2) +

                (weight_table[t11e][t21] * aux_carry_over_table[t11e][t21]**2) + 
                (weight_table[t21e][t11] * aux_carry_over_table[t21e][t11]**2) + 
                (weight_table[t21][t11d] * aux_carry_over_table[t21][t11d]**2) +
                (weight_table[t11][t21d] * aux_carry_over_table[t11][t21d]**2)     
            )

        if len(times) > 1:
            r01 = times[0]
            r02 = times[-1]
            
            t11 = aux_schedule[t1][r01]
            t21 = aux_schedule[t2][r01]

            t12 = aux_schedule[t1][r02]
            t22 = aux_schedule[t2][r02]

            if r01 == 0:
                t11e = aux_schedule[t1][-1]
                t21e = aux_schedule[t2][-1]

            else:
                t11e = aux_schedule[t1][r01-1]
                t21e = aux_schedule[t2][r01-1]

            if r02 == n_times-2:

                t12d = aux_schedule[t1][0]
                t22d = aux_schedule[t2][0]   
            else:

                t12d = aux_schedule[t1][r02+1]
                t22d = aux_schedule[t2][r02+1]

            new_obj -= (
                (weight_table[t11e][t11] * aux_carry_over_table[t11e][t11]**2) + 
                (weight_table[t21e][t21] * aux_carry_over_table[t21e][t21]**2) + 
                (weight_table[t12][t12d] * aux_carry_over_table[t12][t12d]**2) +
                (weight_table[t22][t22d] * aux_carry_over_table[t22][t22d]**2) +

                (weight_table[t11e][t21] * aux_carry_over_table[t11e][t21]**2) + 
                (weight_table[t21e][t11] * aux_carry_over_table[t21e][t11]**2) + 
                (weight_table[t22][t12d] * aux_carry_over_table[t22][t12d]**2) +
                (weight_table[t12][t22d] * aux_carry_over_table[t12][t22d]**2)     
            )

            aux_carry_over_table[t11e][t11] -=1
            aux_carry_over_table[t21e][t21] -=1
            aux_carry_over_table[t12][t12d] -=1
            aux_carry_over_table[t22][t22d] -=1

            aux_carry_over_table[t11e][t21] +=1
            aux_carry_over_table[t21e][t11] +=1
            aux_carry_over_table[t22][t12d] +=1
            aux_carry_over_table[t12][t22d] +=1       

            new_obj += (
                (weight_table[t11e][t11] * aux_carry_over_table[t11e][t11]**2) + 
                (weight_table[t21e][t21] * aux_carry_over_table[t21e][t21]**2) + 
                (weight_table[t12][t12d] * aux_carry_over_table[t12][t12d]**2) +
                (weight_table[t22][t22d] * aux_carry_over_table[t22][t22d]**2) +

                (weight_table[t11e][t21] * aux_carry_over_table[t11e][t21]**2) + 
                (weight_table[t21e][t11] * aux_carry_over_table[t21e][t11]**2) + 
                (weight_table[t22][t12d] * aux_carry_over_table[t22][t12d]**2) +
                (weight_table[t12][t22d] * aux_carry_over_table[t12][t22d]**2)     
            )

    return new_obj, aux_carry_over_table


def obj_pts2(obj,schedule,r,t1,t2,weight_table,carry_over_table):
    aux_schedule = [x[:] for x in schedule]
    pts(aux_schedule,r,t1,t2)
    new_obj,aux_carry_over_table = objetivo(aux_schedule,weight_table)

    return new_obj, aux_carry_over_table