from objetivo import objetivo
from partial_round_swap.prs import prs

def min_prs_test(n,schedule,weight_table,obj):
    incremento = -1
    obj_minimo = obj
    while incremento < 0:
        obj_inicial = obj_minimo
        for r1 in range(n-1):
            for r2 in range(n-1):
                if r1 < r2:
                    for t in range(n):
                        prs(schedule,t,r1,r2)
                        obj,carry_over_table = objetivo(schedule,weight_table)
                        prs(schedule,t,r1,r2)
                        if obj < obj_minimo:
                            obj_minimo = obj
                            best_r1 = r1
                            best_r2 = r2
                            best_t = t
        incremento = obj_minimo - obj_inicial
        if incremento < 0:
            prs(schedule,best_t,best_r1,best_r2)
    print('obj prs min test:',obj_minimo)