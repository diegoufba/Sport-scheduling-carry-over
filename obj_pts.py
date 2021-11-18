from geradores.circle import circle_method
from geradores.vizing_professor import vizing
from objetivo import objetivo
from readInstanceWeight import getInstance

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

    return new_obj, aux_carry_over_table



weight_table, n = getInstance(f'instances/inst{10}linearperturbacaoA.xml')
schedule = vizing(n-1)
#schedule = circle_method(10)
obj,carry_over_table = objetivo(schedule,weight_table)

#schedule = vizing(10)
r = 0
t1 = 0
t2 = 1
obj_pts(obj,schedule,r,t1,t2,weight_table,carry_over_table)