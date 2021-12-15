import random
from partial_round_swap.prs import prs
from partial_round_swap.obj_prs import obj_prs

def pertubacao(obj,schedule,weight_table,carry_over_table):
    n = len(schedule)
    t = random.sample(range(n),1)[0]
    r1,r2=random.sample(range(n-1),2)
    obj,carry_over_table = obj_prs(obj,schedule,t,r1,r2,weight_table,carry_over_table)
    prs(schedule,t,r1,r2)
    return obj