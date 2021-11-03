from team_swap.ts import ts
from team_swap.obj_ts import obj_ts

def min_ts(n,schedule,weight_table,carry_over_table,obj):
    incremento = -1
    obj_minimo = obj
    while incremento < 0:
        obj_inicial = obj_minimo
        for t1 in range(n-1):
            for t2 in range(t1+1,n):
                obj,c = obj_ts(obj_inicial,schedule,t1,t2,weight_table,carry_over_table)
                if obj < obj_minimo:
                    obj_minimo = obj
                    best_t1 = t1
                    best_t2 = t2
                    best_carry_over_table = c
        incremento = obj_minimo - obj_inicial
        if incremento < 0:
            ts(schedule,best_t1,best_t2)
            carry_over_table = best_carry_over_table
    print('obj ts min:',obj_minimo)