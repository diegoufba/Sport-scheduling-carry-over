import copy
def rs(schedule,r1,r2):
    for i in range (len(schedule)):
        # Troca de round
        schedule[i][r1] ,schedule[i][r2] = schedule[i][r2] ,schedule[i][r1]

def obj_rs(obj,schedule,r1,r2,weight_table,carry_over_table):
    new_obj = obj
    aux_carry_over_table = copy.deepcopy(carry_over_table)
    n_times = len(schedule)

    if r1 == 0 and r2==n_times-2:
        for i in range (n_times):
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
        for i in range (n_times):
        
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
        for i in range (n_times):
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
        for i in range (n_times):
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


def obj_rs2(obj,schedule,r1,r2,weight_table,carry_over_table):
    n_times = len(schedule)
    for i in range (n_times):

        pos_te1 = r1-1
        pos_td2 = r2+1

        if r1 == 0:
            pos_te1 = n_times-2
        if r2 == n_times-2:
            pos_td2 = 0

        te1 = schedule[i][pos_te1]
        t1 = schedule[i][r1]
        td1 = schedule[i][r1+1]
        
        te2 = schedule[i][r2-1]
        t2 = schedule[i][r2]
        td2 = schedule[i][pos_td2]

        obj -= (
            (weight_table[te1][t1] * carry_over_table[te1][t1]**2) + 
            (weight_table[t1][td1] * carry_over_table[t1][td1]**2) + 
            (weight_table[te1][t2] * carry_over_table[te1][t2]**2) +
            (weight_table[t2][td1] * carry_over_table[t2][td1]**2) +
            (weight_table[te2][t2] * carry_over_table[te2][t2]**2) +
            (weight_table[t2][td2] * carry_over_table[t2][td2]**2) +
            (weight_table[te2][t1] * carry_over_table[te2][t1]**2) +
            (weight_table[t1][td2] * carry_over_table[t1][td2]**2)
        )

        carry_over_table[te1][t1] -= 1
        carry_over_table[t1][td1] -= 1
        carry_over_table[te1][t2] += 1
        carry_over_table[t2][td1] += 1

        carry_over_table[te2][t2] -= 1
        carry_over_table[t2][td2] -= 1
        carry_over_table[te2][t1] += 1
        carry_over_table[t1][td2] += 1
        
        obj += (
            (weight_table[te1][t1] * carry_over_table[te1][t1]**2) + 
            (weight_table[t1][td1] * carry_over_table[t1][td1]**2) + 
            (weight_table[te1][t2] * carry_over_table[te1][t2]**2) +
            (weight_table[t2][td1] * carry_over_table[t2][td1]**2) +
            (weight_table[te2][t2] * carry_over_table[te2][t2]**2) +
            (weight_table[t2][td2] * carry_over_table[t2][td2]**2) +
            (weight_table[te2][t1] * carry_over_table[te2][t1]**2) +
            (weight_table[t1][td2] * carry_over_table[t1][td2]**2)
        )
        
    return obj,carry_over_table

            # a = [
            #     (weight_table[t1][t2],carry_over_table[t1][t2]),
            #     (weight_table[te1][t1],carry_over_table[te1][t1]),
            #     (weight_table[t2][td2],carry_over_table[t2][td2])
            # ]

            # b = [
            #     (weight_table[t2][t1],carry_over_table[t2][t1]),
            #     (weight_table[t1][td2],carry_over_table[t1][td2]),
            #     (weight_table[te1][t2],carry_over_table[te1][t2])
            # ]

            # for carry_over in a:
            #     w,c = carry_over
            #     obj += (w*(c-1)**2)-(w*c**2)

            # for carry_over in b:
            #     w,c = carry_over
            #     obj += (w*(c+1)**2)-(w*c**2)
