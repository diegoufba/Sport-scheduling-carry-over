from team_swap.ts import ts
from team_swap.obj_ts import obj_ts

def min_ts(n,schedule,weight_table,carry_over_table,obj):
    obj_minimo = obj
    for t1 in range(n):
        for t2 in range(n):
            if t1 < t2:
                obj,c = obj_ts(obj_minimo,schedule,t1,t2,weight_table,carry_over_table)
                #print(f'{t1}{t2}: {obj} ')
                if obj >= obj_minimo:
                    pass
                else:
                    obj_minimo = obj
                    carry_over_table = c
                    ts(schedule,t1,t2)
    print('obj ts min:',obj_minimo)