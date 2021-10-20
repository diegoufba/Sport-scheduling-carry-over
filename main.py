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

# print('carry over inicial')
# for line in carry_over_table:
#     print(line)

r1 ,r2 = 7,8

obj,c = obj_rs(obj,schedule,r1,r2,weight_table,carry_over_table[:])
print('objetivo teste:',obj)

# print('carry over teste')
# for line in c:
#     print(line)

schedule = rs(schedule,r1,r2)

obj,carry_over_table = objetivo(schedule,weight_table)

# print()
# print('carry over real')
# for line in carry_over_table:
#     print(line)
print('objetivo real:',obj)

# for line in schedule:
#     print(line)

#cProfile.run('circle_method(n)')

# Calcula a funcao objetivo


# Faz a troca parcial de rodadas
#schedule = prs(schedule,0,1,3)

# Faz a troca parcial de times
#schedule = pts(schedule,1,0,1)
#cProfile.run('pts(schedule,1,0,1)')


#obj = objetivo(schedule,weight_table)

#cProfile.run('objetivo(schedule,weight_table)')

#print(f'obj2: {obj}')

# for line in pts(schedule,0,2,3):
#     print(line)

save_solution(schedule)