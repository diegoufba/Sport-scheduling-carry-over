from objetivo import objetivo
from team_swap.ts import ts

def min_ts_test(n,schedule,weight_table,obj):
    obj_minimo = obj
    for t1 in range(n):
        for t2 in range(n):
            if t1 < t2:
                ts(schedule,t1,t2)
                obj,carry_over_table = objetivo(schedule,weight_table)
                #print(f'{t1}{t2}: {obj} ')
                if obj < obj_minimo:
                    obj_minimo = obj
                else:
                    ts(schedule,t1,t2)
    print('obj ts min test:',obj_minimo)