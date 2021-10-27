import copy

def obj_ts(obj,schedule,t1,t2,weight_table,carry_over_table):
    new_obj = obj
    aux_carry_over_table = copy.deepcopy(carry_over_table)
    n_times = len(schedule)

    for i in range(n_times):
        if i == t1 or i == t2:
            if i== t1:
                r = schedule[i].index(t2)
            else:
                r = schedule[i].index(t1)
                t1,t2 = t2,t1
            if r == 0:
                te2 = schedule[i][n_times-2]
                td2 = schedule[i][r+1]
            elif r == n_times-2:
                te2 = schedule[i][r-1]
                td2 = schedule[i][0]
            else:
                te2 = schedule[i][r -1]
                td2 = schedule[i][r + 1]
            new_obj -= (
                (weight_table[te2][t2] * aux_carry_over_table[te2][t2]**2) + 
                (weight_table[t2][td2] * aux_carry_over_table[t2][td2]**2) +
                (weight_table[te2][t1] * aux_carry_over_table[te2][t1]**2) + 
                (weight_table[t1][td2] * aux_carry_over_table[t1][td2]**2)
            )
            aux_carry_over_table[te2][t2] -=1
            aux_carry_over_table[t2][td2] -=1

            aux_carry_over_table[te2][t1] +=1
            aux_carry_over_table[t1][td2] +=1 

            new_obj += (
                (weight_table[te2][t2] * aux_carry_over_table[te2][t2]**2) + 
                (weight_table[t2][td2] * aux_carry_over_table[t2][td2]**2) +
                (weight_table[te2][t1] * aux_carry_over_table[te2][t1]**2) + 
                (weight_table[t1][td2] * aux_carry_over_table[t1][td2]**2)
            )        
        else:
            r1 = schedule[i].index(t1)
            r2 = schedule[i].index(t2)
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