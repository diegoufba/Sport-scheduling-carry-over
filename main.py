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
print('obj circulo:',obj)

resp2 = []
resp1 = []
# Round Swap para Objetivo Minimo
obj_minimo = obj
for r1 in range(n-2):
    for r2 in range(n-2):
        if r1 < r2:
            obj = obj_rs(obj_minimo,schedule,r1,r2,weight_table,carry_over_table)
            resp1.append((r1,r2,obj))
            if obj < obj_minimo:
                obj_minimo = obj
                rs(schedule,r1,r2)
print(obj_minimo)
save_solution(schedule)

# Round Swap para Objetivo Minimo
schedule = circle_method(n)
obj,carry_over_table = objetivo(schedule,weight_table)
obj_minimo = obj
for r1 in range(n-2):
    for r2 in range(n-2):
        if r1 < r2:
            rs(schedule,r1,r2)
            obj,carry_over_table = objetivo(schedule,weight_table)
            resp2.append((r1,r2,obj))
            #print(r1,r2,obj)
            if obj < obj_minimo:
                obj_minimo = obj
            else:
                rs(schedule,r1,r2)
print(obj_minimo)

for i in range(len(resp1)):
    print(f'{resp2[i][0]} {resp2[i][1]} {resp2[i][2]} {resp1[i][2]}')
