import cProfile

from circle import circle_method
from objetivo import objetivo
from readInstanceWeight import getInstance
from saveSchedule import save_solution
from rs_obj_min import min_rs
from rs_obj_min_test import min_rs_test
from prs_obj_min_test import min_prs_test
from ts_obj_min import min_ts_test
from pts_obj_min_test import min_pts_test

# Escolhe o tamanho da instancia
# Valores disponiveis: 6,10,12,14,16,18,20
instance_size = 10

# Ler a instancia
weight_table, n = getInstance(f'instances/inst{instance_size}linearperturbacaoA.xml')

# Gera a solucao pelo metodo do circulo
schedule = circle_method(n)

# Calcula a funcao Objetivo do circulo e a tabela de carry over
obj,carry_over_table = objetivo(schedule,weight_table)
print('obj circulo:',obj)

# Escolhe a operacao
operacao ='rs'

# Round Swap Objetivo Minimo
if operacao == 'rs':
    min_rs(n,schedule,weight_table,carry_over_table,obj)
    #min_rs_test(n,schedule,weight_table,obj)

# Partial Round Swap Objetivo Minimo
if operacao == 'prs':
    min_prs_test(n,schedule,weight_table,obj)

# Team Swap Objetivo Minimo
if operacao == 'ts':
    min_ts_test(n,schedule,weight_table,obj)

# Partial Team Swap Objetivo Minimo
if operacao == 'pts':
    min_pts_test(n,schedule,weight_table,obj)

# Salva a solucao final
save_solution(schedule)
