from round_swap import rs,obj_rs

def min_rs(n,schedule,weight_table,carry_over_table,obj):

    n_rounds = n-1
    obj_minimo = obj

    for r1 in range(n_rounds):
        for r2 in range(n_rounds):
            if r1 < r2:
                obj,c = obj_rs(obj_minimo,schedule,r1,r2,weight_table,carry_over_table)
                if obj >= obj_minimo:
                    pass
                else:
                    obj_minimo = obj
                    carry_over_table = c
                    rs(schedule,r1,r2)
    print('obj rs min:',obj_minimo)
