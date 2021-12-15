# from objetivo import objetivo
# from partial_round_swap.prs import prs

def obj_prs(obj,schedule,t,r1,r2,weight_table,carry_over_table):
    new_obj = obj
    aux_carry_over_table = [x[:] for x in carry_over_table]
    n_times = len(schedule)

    # Determina os times que serao trocados entre r1 e r2
    initial_team = t
    times = []
    for i in range (n_times):
        times.append(t)
        if i % 2 != 0:
            t = schedule[t][r1]
        else:
            t = schedule[t][r2]
        if t == initial_team:
            break

    if r1 == 0 and r2==n_times-2:
        for i in times:
            t1 = schedule[i][r1]
            t2 = schedule[i][r2]

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
        for i in times:
        
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
        for i in times:
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
        for i in times:
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


# def obj_prs_test(obj,schedule,t,r1,r2,weight_table,carry_over_table):
#     aux_schedule = [x[:] for x in schedule]
#     prs(schedule,t,r1,r2)
#     new_obj,aux_carry_over_table = objetivo(aux_schedule,weight_table)

#     return new_obj, aux_carry_over_table