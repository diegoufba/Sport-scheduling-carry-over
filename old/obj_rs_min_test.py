from objetivo import objetivo
from round_swap.rs import rs

# Round Swap para Objetivo Minimo - Teste
def min_rs_test(n,schedule,weight_table,obj):
    incremento = -1
    obj_minimo = obj
    while incremento < 0:
        obj_inicial = obj_minimo
        for r1 in range(n-1):
            for r2 in range(n-1):
                if r1 < r2:
                    rs(schedule,r1,r2)
                    obj,carry_over_table = objetivo(schedule,weight_table)
                    rs(schedule,r1,r2)
                    if obj < obj_minimo:
                        obj_minimo = obj
                        best_r1 = r1
                        best_r2 = r2
        incremento = obj_minimo - obj_inicial
        if incremento < 0:
            rs(schedule,best_r1,best_r2)
    print('obj rs min test:',obj_minimo)