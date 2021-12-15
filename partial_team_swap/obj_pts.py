# from objetivo import objetivo
# from partial_team_swap.pts import pts
import more_itertools as mit

def obj_pts(obj,schedule,r,t1,t2,weight_table,carry_over_table):    

    new_obj = obj
    aux_carry_over_table = [x[:] for x in carry_over_table]
    n_times = len(schedule)

    initial_round = r
    rounds = [r]
    for i in range (len(schedule)-1):
        next_r = schedule[t1].index(schedule[t2][r])

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

    for times in times_consecutivos:
        if len(times) == 1:
            r01 = times[0]

            t11 = schedule[t1][r01]
            t21 = schedule[t2][r01]
            
            if r01 == 0:
                t11e = schedule[t1][-1]
                t21e = schedule[t2][-1]

            else:
                t11e = schedule[t1][r01-1]
                t21e = schedule[t2][r01-1]

            if r01 == n_times-2:

                t11d = schedule[t1][0]
                t21d = schedule[t2][0]   
            else:

                t11d = schedule[t1][r01+1]
                t21d = schedule[t2][r01+1]

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
            
            t11 = schedule[t1][r01]
            t21 = schedule[t2][r01]

            t12 = schedule[t1][r02]
            t22 = schedule[t2][r02]

            if r01 == 0:
                t11e = schedule[t1][-1]
                t21e = schedule[t2][-1]

            else:
                t11e = schedule[t1][r01-1]
                t21e = schedule[t2][r01-1]

            if r02 == n_times-2:

                t12d = schedule[t1][0]
                t22d = schedule[t2][0]   
            else:

                t12d = schedule[t1][r02+1]
                t22d = schedule[t2][r02+1]

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
    for i in range(n_times):     
        if i != t1 and i!= t2:
            r1 = schedule[i].index(t1)
            r2 = schedule[i].index(t2)
            if r1 not in rounds:
                continue
            if r1 > r2:
                r1,r2 = r2,r1
                t1,t2 = t2,t1
            if r1 == 0 and r2==n_times-2:
                td1 = schedule[i][r1+1]
                te2 = schedule[i][r2-1]

                new_obj -= (
                    (weight_table[t2][t1] * aux_carry_over_table[t2][t1]**2) + 
                    (weight_table[t1][td1] * aux_carry_over_table[t1][td1]**2) + 
                    (weight_table[te2][t2] * aux_carry_over_table[te2][t2]**2) +

                    (weight_table[t1][t2] * aux_carry_over_table[t1][t2]**2) +
                    (weight_table[t2][td1] * aux_carry_over_table[t2][td1]**2) +
                    (weight_table[te2][t1] * aux_carry_over_table[te2][t1]**2)
                )

                aux_carry_over_table[t2][t1] -=1
                aux_carry_over_table[t1][td1] -=1
                aux_carry_over_table[te2][t2] -=1
                aux_carry_over_table[t1][t2] +=1
                aux_carry_over_table[t2][td1] +=1
                aux_carry_over_table[te2][t1] +=1

                new_obj += (
                    (weight_table[t2][t1] * aux_carry_over_table[t2][t1]**2) + 
                    (weight_table[t1][td1] * aux_carry_over_table[t1][td1]**2) + 
                    (weight_table[te2][t2] * aux_carry_over_table[te2][t2]**2) +

                    (weight_table[t1][t2] * aux_carry_over_table[t1][t2]**2) +
                    (weight_table[t2][td1] * aux_carry_over_table[t2][td1]**2) +
                    (weight_table[te2][t1] * aux_carry_over_table[te2][t1]**2)
                )
            elif r2-r1 == 1:
            
                t1 = schedule[i][r1]
                t2 = schedule[i][r2]

                if r1 != 0:
                    te1 = schedule[i][r1-1]
                else:
                    te1 = schedule[i][n_times-2]
                if r2 != n_times-2:
                    td2 = schedule[i][r2+1]
                else:
                    td2 = schedule[i][0]
                
                new_obj -= (
                    (weight_table[t1][t2] * aux_carry_over_table[t1][t2]**2) + 
                    (weight_table[te1][t1] * aux_carry_over_table[te1][t1]**2) + 
                    (weight_table[t2][td2] * aux_carry_over_table[t2][td2]**2) +

                    (weight_table[t2][t1] * aux_carry_over_table[t2][t1]**2) +
                    (weight_table[t1][td2] * aux_carry_over_table[t1][td2]**2) +
                    (weight_table[te1][t2] * aux_carry_over_table[te1][t2]**2)
                )

                aux_carry_over_table[t1][t2] -=1
                aux_carry_over_table[te1][t1] -=1
                aux_carry_over_table[t2][td2] -=1
                aux_carry_over_table[t2][t1] +=1
                aux_carry_over_table[t1][td2] +=1
                aux_carry_over_table[te1][t2] +=1

                new_obj += (
                    (weight_table[t1][t2] * aux_carry_over_table[t1][t2]**2) + 
                    (weight_table[te1][t1] * aux_carry_over_table[te1][t1]**2) + 
                    (weight_table[t2][td2] * aux_carry_over_table[t2][td2]**2) +

                    (weight_table[t2][t1] * aux_carry_over_table[t2][t1]**2) +
                    (weight_table[t1][td2] * aux_carry_over_table[t1][td2]**2) +
                    (weight_table[te1][t2] * aux_carry_over_table[te1][t2]**2)
                )
            elif r2-r1 == 2:
                t1 = schedule[i][r1]
                t2 = schedule[i][r2]

                if r1 != 0:
                    te1 = schedule[i][r1-1]
                else:
                    te1 = schedule[i][n_times-2]

                td1 = schedule[i][r1+1]

                if r2 != n_times-2:
                    td2 = schedule[i][r2+1]
                else:
                    td2 = schedule[i][0]

                new_obj -= (
                    (weight_table[te1][t1] * aux_carry_over_table[te1][t1]**2) + 
                    (weight_table[t1][td1] * aux_carry_over_table[t1][td1]**2) + 
                    (weight_table[td1][t2] * aux_carry_over_table[td1][t2]**2) +
                    (weight_table[t2][td2] * aux_carry_over_table[t2][td2]**2) +

                    (weight_table[td1][t1] * aux_carry_over_table[td1][t1]**2) +
                    (weight_table[te1][t2] * aux_carry_over_table[te1][t2]**2)+
                    (weight_table[t2][td1] * aux_carry_over_table[t2][td1]**2)+
                    (weight_table[t1][td2] * aux_carry_over_table[t1][td2]**2)
                )

                aux_carry_over_table[te1][t1] -=1
                aux_carry_over_table[t1][td1] -=1
                aux_carry_over_table[td1][t2] -=1
                aux_carry_over_table[t2][td2] -=1

                aux_carry_over_table[td1][t1] +=1
                aux_carry_over_table[te1][t2] +=1
                aux_carry_over_table[t2][td1] +=1
                aux_carry_over_table[t1][td2] +=1

                new_obj += (
                    (weight_table[te1][t1] * aux_carry_over_table[te1][t1]**2) + 
                    (weight_table[t1][td1] * aux_carry_over_table[t1][td1]**2) + 
                    (weight_table[td1][t2] * aux_carry_over_table[td1][t2]**2) +
                    (weight_table[t2][td2] * aux_carry_over_table[t2][td2]**2) +

                    (weight_table[td1][t1] * aux_carry_over_table[td1][t1]**2) +
                    (weight_table[te1][t2] * aux_carry_over_table[te1][t2]**2)+
                    (weight_table[t2][td1] * aux_carry_over_table[t2][td1]**2)+
                    (weight_table[t1][td2] * aux_carry_over_table[t1][td2]**2)
                )

            elif r2-r1 >= 3:
                t1 = schedule[i][r1]
                t2 = schedule[i][r2]

                td1 = schedule[i][r1+1]
                te2 = schedule[i][r2-1]

                if r1 != 0:
                    te1 = schedule[i][r1-1]
                else:
                    te1 = schedule[i][n_times-2]
                if r2 != n_times-2:
                    td2 = schedule[i][r2+1]
                else:
                    td2 = schedule[i][0]

                new_obj -= (
                    (weight_table[te1][t1] * aux_carry_over_table[te1][t1]**2) + 
                    (weight_table[t1][td1] * aux_carry_over_table[t1][td1]**2) + 
                    (weight_table[te2][t2] * aux_carry_over_table[te2][t2]**2) +
                    (weight_table[t2][td2] * aux_carry_over_table[t2][td2]**2) +

                    (weight_table[te1][t2] * aux_carry_over_table[te1][t2]**2) +
                    (weight_table[t2][td1] * aux_carry_over_table[t2][td1]**2)+
                    (weight_table[te2][t1] * aux_carry_over_table[te2][t1]**2)+
                    (weight_table[t1][td2] * aux_carry_over_table[t1][td2]**2)
                )

                aux_carry_over_table[te1][t1] -=1
                aux_carry_over_table[t1][td1] -=1
                aux_carry_over_table[te2][t2] -=1
                aux_carry_over_table[t2][td2] -=1

                aux_carry_over_table[te1][t2] +=1
                aux_carry_over_table[t2][td1] +=1
                aux_carry_over_table[te2][t1] +=1
                aux_carry_over_table[t1][td2] +=1

                new_obj += (
                    (weight_table[te1][t1] * aux_carry_over_table[te1][t1]**2) + 
                    (weight_table[t1][td1] * aux_carry_over_table[t1][td1]**2) + 
                    (weight_table[te2][t2] * aux_carry_over_table[te2][t2]**2) +
                    (weight_table[t2][td2] * aux_carry_over_table[t2][td2]**2) +

                    (weight_table[te1][t2] * aux_carry_over_table[te1][t2]**2) +
                    (weight_table[t2][td1] * aux_carry_over_table[t2][td1]**2)+
                    (weight_table[te2][t1] * aux_carry_over_table[te2][t1]**2)+
                    (weight_table[t1][td2] * aux_carry_over_table[t1][td2]**2)
                )
    return new_obj, aux_carry_over_table


# def obj_pts_test(obj,schedule,r,t1,t2,weight_table,carry_over_table):
#     pts(schedule,r,t1,t2)
#     new_obj,aux_carry_over_table = objetivo(schedule,weight_table)

#     return new_obj, aux_carry_over_table