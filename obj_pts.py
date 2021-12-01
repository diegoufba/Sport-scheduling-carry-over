from geradores.circle import circle_method
from geradores.vizing_professor import vizing
from objetivo import objetivo
from readInstanceWeight import getInstance
from partial_team_swap.pts import pts

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
    print(rounds)

    aux_schedule = [x[:] for x in schedule]

    for r in rounds:
        t3 = aux_schedule[t1][r]
        t4 = aux_schedule[t2][r]
        
        i5,i6 = [i for i in range(n_times) if aux_schedule[i][r] == t1 or aux_schedule[i][r] == t2]

        t5 = aux_schedule[i5][r]
        t6 = aux_schedule[i6][r]

        if r == 0:
            t3e = aux_schedule[t1][n_times-2]
            t4e = aux_schedule[t2][n_times-2]

            t5e = aux_schedule[i5][n_times-2]
            t6e = aux_schedule[i6][n_times-2]
        else:
            t3e = aux_schedule[t1][r-1]
            t4e = aux_schedule[t2][r-1]
            
            t5e = aux_schedule[i5][r-1]
            t6e = aux_schedule[i6][r-1]

        if r == n_times-2:
            t3d = aux_schedule[t1][0]
            t4d = aux_schedule[t2][0]
            
            t5d = aux_schedule[i5][0]
            t6d = aux_schedule[i6][0]  

        else:
            t3d = aux_schedule[t1][r+1]
            t4d = aux_schedule[t2][r+1]    
            
            t5d = aux_schedule[i5][r+1]
            t6d = aux_schedule[i6][r+1]    

        new_obj -= (
            (weight_table[t3e][t3] * aux_carry_over_table[t3e][t3]**2) + 
            (weight_table[t3][t3d] * aux_carry_over_table[t3][t3d]**2) + 
            (weight_table[t4e][t4] * aux_carry_over_table[t4e][t4]**2) +
            (weight_table[t4][t4d] * aux_carry_over_table[t4][t4d]**2) +

            (weight_table[t3e][t4] * aux_carry_over_table[t3e][t4]**2) + 
            (weight_table[t4][t3d] * aux_carry_over_table[t4][t3d]**2) + 
            (weight_table[t4e][t3] * aux_carry_over_table[t4e][t3]**2) +
            (weight_table[t3][t4d] * aux_carry_over_table[t3][t4d]**2) 

            # (weight_table[t5e][t5] * aux_carry_over_table[t5e][t5]**2) + 
            # (weight_table[t5][t5d] * aux_carry_over_table[t5][t5d]**2) + 
            # (weight_table[t6e][t6] * aux_carry_over_table[t6e][t6]**2) +
            # (weight_table[t6][t6d] * aux_carry_over_table[t6][t6d]**2) +

            # (weight_table[t5e][t6] * aux_carry_over_table[t5e][t6]**2) + 
            # (weight_table[t6][t5d] * aux_carry_over_table[t6][t5d]**2) + 
            # (weight_table[t6e][t5] * aux_carry_over_table[t6e][t5]**2) +
            # (weight_table[t5][t6d] * aux_carry_over_table[t5][t6d]**2) 
        )
        aux_carry_over_table[t3e][t3] -=1
        aux_carry_over_table[t3][t3d] -=1
        aux_carry_over_table[t4e][t4] -=1
        aux_carry_over_table[t4][t4d] -=1

        aux_carry_over_table[t3e][t4] +=1
        aux_carry_over_table[t4][t3d] +=1
        aux_carry_over_table[t4e][t3] +=1
        aux_carry_over_table[t3][t4d] +=1

        # aux_carry_over_table[t5e][t5] -=1
        # aux_carry_over_table[t5][t5d] -=1
        # aux_carry_over_table[t6e][t6] -=1
        # aux_carry_over_table[t6][t6d] -=1

        # aux_carry_over_table[t5e][t6] +=1
        # aux_carry_over_table[t6][t5d] +=1
        # aux_carry_over_table[t6e][t5] +=1
        # aux_carry_over_table[t5][t6d] +=1

        new_obj += (
            (weight_table[t3e][t3] * aux_carry_over_table[t3e][t3]**2) + 
            (weight_table[t3][t3d] * aux_carry_over_table[t3][t3d]**2) + 
            (weight_table[t4e][t4] * aux_carry_over_table[t4e][t4]**2) +
            (weight_table[t4][t4d] * aux_carry_over_table[t4][t4d]**2) +

            (weight_table[t3e][t4] * aux_carry_over_table[t3e][t4]**2) + 
            (weight_table[t4][t3d] * aux_carry_over_table[t4][t3d]**2) + 
            (weight_table[t4e][t3] * aux_carry_over_table[t4e][t3]**2) +
            (weight_table[t3][t4d] * aux_carry_over_table[t3][t4d]**2) 

            # (weight_table[t5e][t5] * aux_carry_over_table[t5e][t5]**2) + 
            # (weight_table[t5][t5d] * aux_carry_over_table[t5][t5d]**2) + 
            # (weight_table[t6e][t6] * aux_carry_over_table[t6e][t6]**2) +
            # (weight_table[t6][t6d] * aux_carry_over_table[t6][t6d]**2) +

            # (weight_table[t5e][t6] * aux_carry_over_table[t5e][t6]**2) + 
            # (weight_table[t6][t5d] * aux_carry_over_table[t6][t5d]**2) + 
            # (weight_table[t6e][t5] * aux_carry_over_table[t6e][t5]**2) +
            # (weight_table[t5][t6d] * aux_carry_over_table[t5][t6d]**2) 
        )

        aux_schedule[t1][r],aux_schedule[t2][r] = aux_schedule[t2][r],aux_schedule[t1][r]
        #aux_schedule[i5][r],aux_schedule[i6][r] = aux_schedule[i6][r],aux_schedule[i5][r]

    print(new_obj)
    print(aux_carry_over_table)
    return new_obj, aux_carry_over_table



weight_table, n = getInstance(f'instances/inst{6}linearperturbacaoA.xml')
#schedule = vizing(n-1)
schedule = circle_method(6)
obj,carry_over_table = objetivo(schedule,weight_table)
print(obj)

#1,3
r = 0
t1 = 1
t2 = 5
obj_pts(obj,schedule,r,t1,t2,weight_table,carry_over_table)

pts(schedule,r,t1,t2)
obj,carry_over_table = objetivo(schedule,weight_table)
print(obj)
print(carry_over_table)
