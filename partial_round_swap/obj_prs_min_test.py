from objetivo import objetivo
from partial_round_swap.prs import prs

def min_prs_test(n,schedule,weight_table,obj):
    obj_minimo = obj
    for r1 in range(n-1):
        for r2 in range(n-1):
            if r1 < r2:
                for t in range(n):
                    prs(schedule,t,r1,r2)
                    obj,carry_over_table = objetivo(schedule,weight_table)
                    #print(f'{r1}{r2}{t}: {obj} ')
                    if obj < obj_minimo:
                        obj_minimo = obj
                    else:
                        prs(schedule,t,r1,r2)
    print('obj prs min test:',obj_minimo)