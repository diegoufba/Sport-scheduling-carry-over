from partial_round_swap.prs import prs
from partial_round_swap.obj_prs import obj_prs

def min_prs(n,schedule,weight_table,carry_over_table,obj):
    incremento = -1
    obj_minimo = obj
    while incremento < 0:
        obj_inicial = obj_minimo
        for r1 in range(n-2):
            for r2 in range(r1+1,n-1):
                for t in range(n):
                    obj,c = obj_prs(obj_inicial,schedule,t,r1,r2,weight_table,carry_over_table)
                    if obj < obj_minimo:
                        obj_minimo = obj
                        best_r1 = r1
                        best_r2 = r2
                        best_t = t
                        best_carry_over_table = c
        incremento = obj_minimo - obj_inicial
        if incremento < 0:
            prs(schedule,best_t,best_r1,best_r2)
            carry_over_table = best_carry_over_table
    print('obj prs min:',obj_minimo)
