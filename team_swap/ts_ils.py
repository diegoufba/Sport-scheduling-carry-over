import copy
from team_swap.obj_ts_min import min_ts
from round_swap.rs import rs
from round_swap.obj_rs import obj_rs

def ts_ils(n,schedule,weight_table,carry_over_table,obj):
    # Busca Local
    obj = min_ts(n,schedule,weight_table,carry_over_table,obj)
    for r1 in range(n-2):
        for r2 in range(r1+1,n-1):
            # Pertubacao
            pertubado_schedule = copy.deepcopy(schedule)
            pertubado_obj, pertubado_carry_over_table = obj_rs(obj,schedule,r1,r2,weight_table,carry_over_table)
            rs(pertubado_schedule,r1,r2)
            #print('rs:',pertubado_obj)
            # Busca Local
            pertubado_obj = min_ts(n,pertubado_schedule,weight_table,pertubado_carry_over_table,pertubado_obj)
            #print('local:',pertubado_obj)
            if pertubado_obj < obj:
                schedule = pertubado_schedule
                obj = pertubado_obj
                carry_over_table = pertubado_carry_over_table
    print(f'Best obj: {obj}')


