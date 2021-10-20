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

weight_table = [[1]*n]*n


# Gera a solucao pelo metodo do circulo
schedule = circle_method(n)
obj,carry_over_table = objetivo(schedule,weight_table)

n_rounds = len(schedule)-1



best_obj = obj
resp1 = []

for r1 in range(n_rounds):
    for r2 in range(n_rounds):
        s = schedule[:]
        if r1 < r2:
            obj2,c=obj_rs(obj,s,r1,r2,weight_table,carry_over_table)
            if r1 ==0 and r2==4:
                for line in c:
                    print(line)
            rs(s,r1,r2)

            obj,carry_over_table = objetivo(s,weight_table)
            if r1 ==0 and r2==4:
                if c == carry_over_table:
                    print('yes')
                else:
                    print('no')
                for line in schedule:
                    print(line)
                print()
                for line in carry_over_table:
                    print(line)
            resp1.append((r1,r2,obj,obj2))
            if obj >= best_obj:
                rs(s,r1,r2)
            else:
                best_obj = obj
print(best_obj)

# schedule = circle_method(n)
# obj,carry_over_table = objetivo(schedule,weight_table)

# best_obj = obj
# resp2 = []
# for r1 in range(n_rounds):
#     for r2 in range(n_rounds):
#         if r1 < r2:
#             obj,aux_carry_over_table = obj_rs(best_obj,schedule,r1,r2,weight_table,carry_over_table)
#             resp2.append((obj,r1,r2))
#             if obj >= best_obj:
#                 pass
#             else:
#                 best_obj = obj
#                 carry_over_table = aux_carry_over_table[:]
#                 rs(schedule,r1,r2)
# print(best_obj)


for i in range(len(resp1)):
    print(i,resp1[i])
    pass
