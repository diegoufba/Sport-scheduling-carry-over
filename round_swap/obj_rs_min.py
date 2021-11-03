from round_swap.rs import rs
from round_swap.obj_rs import obj_rs

def min_rs(n,schedule,weight_table,carry_over_table,obj):
    incremento = -1
    obj_minimo = obj
    while incremento < 0:
        obj_inicial = obj_minimo

        for r1 in range(n-2):
            for r2 in range(r1+1,n-1):
                obj,c = obj_rs(obj_inicial,schedule,r1,r2,weight_table,carry_over_table)
                if obj < obj_minimo:
                    obj_minimo = obj
                    best_r1 = r1
                    best_r2 = r2
                    best_carry_over_table = c
        incremento = obj_minimo - obj_inicial
        if incremento < 0:
            rs(schedule,best_r1,best_r2)
            carry_over_table = best_carry_over_table
    print('obj rs min:',obj_minimo)
