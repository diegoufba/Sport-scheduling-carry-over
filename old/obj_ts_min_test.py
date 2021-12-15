from objetivo import objetivo
from team_swap.ts import ts

def min_ts_test(n,schedule,weight_table,obj):
    incremento = -1
    obj_minimo = obj
    while incremento < 0:
        obj_inicial = obj_minimo
        for t1 in range(n):
            for t2 in range(n):
                if t1 < t2:
                    ts(schedule,t1,t2)
                    obj,carry_over_table = objetivo(schedule,weight_table)
                    ts(schedule,t1,t2)
                    if obj < obj_minimo:
                        obj_minimo = obj
                        best_t1 = t1
                        best_t2 = t2
        incremento = obj_minimo - obj_inicial
        if incremento < 0:
            ts(schedule,best_t1,best_t2)
    print('obj ts min test:',obj_minimo)