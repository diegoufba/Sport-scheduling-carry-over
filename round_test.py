import cProfile

from circle import circle_method
from objetivo import objetivo
from readInstanceWeight import getInstance
from saveSchedule import save_solution
from partial_round_swap import prs
from partial_team_swap import pts
from round_swap import rs,obj_rs
from team_swap import ts

# Ler a instancia
weight_table, n = getInstance('instances/inst10linearperturbacaoA.xml')

# Gera a solucao pelo metodo do circulo
schedule = circle_method(n)
obj,carry_over_table = objetivo(schedule,weight_table)

n_rounds = len(schedule)-1

best_obj = obj
resp1 = []
for r1 in range(n_rounds):
    for r2 in range(n_rounds):
        if r1 < r2:
            rs(schedule,r1,r2)
            obj,carry_over_table = objetivo(schedule,weight_table)
            # if r1 == 0 and r2 ==2:
            #     print(carry_over_table)
            resp1.append((obj,r1,r2))
            #print(f'{r1}{r2} : {obj}')
            if obj > best_obj:
                rs(schedule,r1,r2)
            else:
                best_obj = obj
print(best_obj)

schedule = circle_method(n)
obj,carry_over_table = objetivo(schedule,weight_table)
best_obj = obj

resp2 = []
for r1 in range(n_rounds):
    for r2 in range(n_rounds):
        if r1 < r2:
            # if r1 == 0 and r2 ==2:
            #     print(c)
            obj,c = obj_rs(best_obj,schedule,r1,r2,weight_table,carry_over_table[:])
            resp2.append((obj,r1,r2))
            #print(f'{r1}{r2} : {obj}')
            if obj > best_obj:
                pass
            else:
                best_obj = obj
                carry_over_table = c
                rs(schedule,r1,r2)
print(best_obj)
save_solution(schedule)

for i in range(len(resp1)):
    print(i,resp1[i],resp2[i])
    pass
