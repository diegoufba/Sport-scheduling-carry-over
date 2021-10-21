from objetivo import objetivo
from partial_round_swap import prs

def min_prs_test(n,schedule,weight_table,obj):
    obj_minimo = obj
    for r1 in range(n-2):
        for r2 in range(n-2):
            if r1 < r2:
                for t in range(n):
                    prs(schedule,t,r1,r2)
                    obj,carry_over_table = objetivo(schedule,weight_table)
                    if obj < obj_minimo:
                        obj_minimo = obj
                    else:
                        prs(schedule,t,r1,r2)
    print('obj prs min test:',obj_minimo)