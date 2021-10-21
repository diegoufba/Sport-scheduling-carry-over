from circle import circle_method
from objetivo import objetivo
from team_swap import ts

def min_ts_test(n,schedule,weight_table,obj):
    obj_minimo = obj
    for t1 in range(n-1):
        for t2 in range(n-1):
            if t1 < t2:
                ts(schedule,t1,t2)
                obj,carry_over_table = objetivo(schedule,weight_table)
                if obj < obj_minimo:
                    obj_minimo = obj
                else:
                    ts(schedule,t1,t2)
    print('obj prs min test:',obj_minimo)