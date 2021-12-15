from saveSchedule import save_solution
import math
from geradores.vizing import vizing
from objetivo import objetivo
from team_swap.obj_ts_min import min_ts
from team_swap.obj_ts_min_test import min_ts_test

from round_swap.rs import rs
from round_swap.obj_rs_min import obj_rs

from partial_round_swap.prs import prs
from partial_round_swap.obj_prs import obj_prs
from pertubacao import pertubacao


def ts_ils(n,weight_table):
    n_iteracoes_max = 10
    n_iteracoes_locais_max = 10
    best_obj = math.inf
    best_schedule = None
    best_carry_over_table = None
    
    for i in range(n_iteracoes_max):
        # Gera solucao Inicial
        schedule = vizing(n-1)
        obj,carry_over_table = objetivo(schedule,weight_table)

        # s'=s
        schedule_linha = [x[:] for x in schedule]
        carry_over_table_linha = [x[:] for x in carry_over_table]
        obj_linha = obj

        n_iteracoes_locais = 0

        while(n_iteracoes_locais < n_iteracoes_locais_max):
            # Busca Local
            obj = min_ts(n,schedule,weight_table,carry_over_table,obj)
            #obj = min_ts_test(n,schedule,weight_table,obj)
            #save_solution(schedule)

            if obj < obj_linha:
                schedule_linha = [x[:] for x in schedule]
                carry_over_table_linha = [x[:] for x in carry_over_table]
                obj_linha = obj

                n_iteracoes_locais = 0

            schedule = [x[:] for x in schedule_linha]
            carry_over_table = [x[:] for x in carry_over_table_linha]
            obj = obj_linha

            #obj = pertubacao(obj,schedule,weight_table,carry_over_table)
            n_iteracoes_locais += 1
        
        if obj_linha < best_obj:
            best_schedule = [x[:] for x in schedule_linha]
            best_carry_over_table = [x[:] for x in carry_over_table_linha]
            best_obj = obj_linha
    save_solution(best_schedule)
    print(best_obj)
            

# def ts_ils(n,schedule,weight_table,carry_over_table,obj):
#     # Busca Local
#     obj = min_ts(n,schedule,weight_table,carry_over_table,obj)
#     for r1 in range(n-2):
#         for r2 in range(r1+1,n-1):
#             # Pertubacao
#             pertubado_schedule = copy.deepcopy(schedule)
#             pertubado_obj, pertubado_carry_over_table = obj_rs(obj,schedule,r1,r2,weight_table,carry_over_table)
#             rs(pertubado_schedule,r1,r2)
#             #print('rs:',pertubado_obj)
#             # Busca Local
#             pertubado_obj = min_ts(n,pertubado_schedule,weight_table,pertubado_carry_over_table,pertubado_obj)
#             #print('local:',pertubado_obj)
#             if pertubado_obj < obj:
#                 schedule = pertubado_schedule
#                 obj = pertubado_obj
#                 carry_over_table = pertubado_carry_over_table
#     print(f'Best obj: {obj}')


