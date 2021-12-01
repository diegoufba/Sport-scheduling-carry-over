from objetivo import objetivo
from partial_team_swap.pts import pts

def obj_pts(obj,schedule,r,t1,t2,weight_table,carry_over_table):
    aux_schedule = [x[:] for x in schedule]
    pts(aux_schedule,r,t1,t2)
    new_obj,aux_carry_over_table = objetivo(aux_schedule,weight_table)

    return new_obj, aux_carry_over_table