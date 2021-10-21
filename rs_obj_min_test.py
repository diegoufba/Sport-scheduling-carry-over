from objetivo import objetivo
from round_swap import rs

# Round Swap para Objetivo Minimo - Teste
def min_rs_test(n,schedule,weight_table,obj):
    
    obj_minimo = obj
    for r1 in range(n-2):
        for r2 in range(n-2):
            if r1 < r2:
                rs(schedule,r1,r2)
                obj,carry_over_table = objetivo(schedule,weight_table)
                if obj < obj_minimo:
                    obj_minimo = obj
                else:
                    rs(schedule,r1,r2)
    print('obj rs min test:',obj_minimo)