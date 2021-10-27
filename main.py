import cProfile
from random import shuffle

from objetivo import objetivo
from readInstanceWeight import getInstance
from saveSchedule import save_solution
from geradores.circle import circle_method
from geradores.vizing_professor import vizing
from round_swap.obj_rs_min import min_rs
from round_swap.obj_rs_min_test import min_rs_test
from partial_round_swap.obj_prs_min import min_prs
from partial_round_swap.obj_prs_min_test import min_prs_test
from team_swap.obj_ts_min_test import min_ts_test
from team_swap.obj_ts_min import min_ts
from partial_team_swap.obj_pts_min_test import min_pts_test

from team_swap.ts import ts
from team_swap.obj_ts import obj_ts

# Escolhe o tamanho da instancia
# Valores disponiveis: 6,10,12,14,16,18,20
instance_size = 10

# Metodos disponiveis: c-circle, v-vizing
metodo = 'c'

# Ler a instancia
weight_table, n = getInstance(f'instances/inst{instance_size}linearperturbacaoA.xml')


if metodo == 'c':
    # Gera a solucao pelo metodo do circulo
    schedule = circle_method(n)
if metodo == 'v':
    # Gera a solucao pelo metodo do vizing
    schedule = vizing(n-1)

# Calcula a funcao Objetivo do circulo e a tabela de carry over
obj,carry_over_table = objetivo(schedule,weight_table)
print(f'obj {metodo}:',obj)

# Escolhe a operacao
operacao ='ts'

# Round Swap Objetivo Minimo
if operacao == 'rs':
    min_rs(n,schedule,weight_table,carry_over_table,obj)
    #min_rs_test(n,schedule,weight_table,obj)

# Partial Round Swap Objetivo Minimo
if operacao == 'prs':
    #min_prs_test(n,schedule,weight_table,obj)
    min_prs(n,schedule,weight_table,carry_over_table,obj)

# Team Swap Objetivo Minimo
if operacao == 'ts':
    min_ts(n,schedule,weight_table,carry_over_table,obj)
    #min_ts_test(n,schedule,weight_table,obj)

# Partial Team Swap Objetivo Minimo
if operacao == 'pts':
    min_pts_test(n,schedule,weight_table,obj)

# Salva a solucao final
save_solution(schedule)
