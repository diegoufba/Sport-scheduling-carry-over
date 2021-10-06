from circle import circle_method
from objetivo import objetivo
from readInstanceWeight import getInstance
from saveSchedule import save_solution
from partial_round_swap import prs
from partial_team_swap import pts

# Ler a instancia
weight_table, n = getInstance('instances/inst6linearperturbacaoA.xml')

# Gera a solucao pelo metodo do circulo
schedule = circle_method(n)

# Calcula a funcao objetivo
obj = objetivo(n,schedule,weight_table)

print(f'obj1: {obj}')

# Faz a troca parcial de rodadas
#schedule = prs(schedule,0,1,3)

# Faz a troca parcial de times
schedule = pts(schedule,1,0,1)

obj = objetivo(n,schedule,weight_table)

print(f'obj2: {obj}')

# for line in pts(schedule,0,2,3):
#     print(line)

save_solution(schedule)