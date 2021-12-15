from geradores.circle import circle_method
from geradores.vizing import vizing
from objetivo import objetivo
from readInstanceWeight import getInstance
from partial_team_swap.pts import pts
import more_itertools as mit
import random

#(obj,schedule,r,t1,t2,weight_table,carry_over_table)
def obj_pts(obj,schedule,r,t1,t2,weight_table,carry_over_table):

    

    new_obj = obj
    aux_carry_over_table = [x[:] for x in carry_over_table]
    n_times = len(schedule)

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

    rounds.sort()
    print(rounds)

    times_consecutivos = [list(x) for x in mit.consecutive_groups(rounds)]
    if times_consecutivos[0][0] == 0 and times_consecutivos[-1][-1] == n_times-2:
        times_consecutivos[-1] += times_consecutivos[0]
        times_consecutivos.pop(0)
    print(times_consecutivos)

    for r in rounds:
        l1,l2 = [i for i in range(n_times) if schedule[i][r] == t1 or schedule[i][r] == t2]
        t11 = schedule[l1][r]
        t21 = schedule[l2][r]
        
        if r == 0:
            t11e = schedule[l1][-1]
            t21e = schedule[l2][-1]

        else:
            t11e = schedule[l1][r-1]
            t21e = schedule[l2][r-1]

        if r == n_times-2:

            t11d = schedule[l1][0]
            t21d = schedule[l2][0]   
        else:

            t11d = schedule[l1][r+1]
            t21d = schedule[l2][r+1]

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

        schedule[l1][r],schedule[l2][r] = schedule[l2][r],schedule[l1][r]

    for times in times_consecutivos:
        if len(times) == 1:
            #print('kkkk')
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

            # print(t11e,t11,t12d)
            # print(t21e,t21,t22d)

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


    #print(rounds)

    # for r in rounds:


    print(new_obj)
    #print(aux_carry_over_table)
    return new_obj, aux_carry_over_table


instancia = 20
weight_table, n = getInstance(f'instances/inst{instancia}linearperturbacaoA.xml')
schedule = vizing(n-1)
#schedule = circle_method(instancia)
#print(schedule)
#schedule = [[3, 2, 1, 5, 4], [2, 5, 0, 4, 3], [1, 0, 4, 3, 5], [0, 4, 5, 2, 1], [5, 3, 2, 1, 0], [4, 1, 3, 0, 2]]
obj,carry_over_table = objetivo(schedule,weight_table)
#print(carry_over_table)
print(obj)

#1,3
r = 0
t1 = 0
t2 = 1
r = random.randint(0,n-2)
t1,t2 = random.sample(range(n),2)
aux_schedule = [x[:] for x in schedule]
new_obj,aux_carry_over_table=obj_pts(obj,aux_schedule,r,t1,t2,weight_table,carry_over_table)

pts(schedule,r,t1,t2)
obj,carry_over_table = objetivo(schedule,weight_table)
print(obj)

# print(aux_carry_over_table)
# print(carry_over_table)
if aux_carry_over_table == carry_over_table:
    print('yes')
else:
    print('no')
