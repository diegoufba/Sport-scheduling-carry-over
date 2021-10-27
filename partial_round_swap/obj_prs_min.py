from partial_round_swap.prs import prs
from partial_round_swap.obj_prs import obj_prs

def min_prs(n,schedule,weight_table,carry_over_table,obj):

    n_rounds = n-1
    obj_minimo = obj

    for r1 in range(n_rounds):
        for r2 in range(n_rounds):
            if r1 < r2:
                for t in range(n):
                    obj,c = obj_prs(obj_minimo,schedule,t,r1,r2,weight_table,carry_over_table)
                    #print(f'{r1}{r2}{t}: {obj} ')
                    if obj >= obj_minimo:
                        pass
                    else:
                        obj_minimo = obj
                        carry_over_table = c
                        prs(schedule,t,r1,r2)
    print('obj rs min:',obj_minimo)
