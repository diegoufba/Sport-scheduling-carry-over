from circle import circle_method
from objetivo import objetivo
from readInstanceWeight import getInstance
from saveSchedule import save_solution
from partial_team_swap import pts

def min_pts_test(n,schedule,weight_table,obj):
    obj_minimo = obj
    for t1 in range(n-1):
        for t2 in range(n-1):
            if t1 < t2:
                for r in range(n-2):
                    pts(schedule,r,t1,t2)
                    obj,carry_over_table = objetivo(schedule,weight_table)
                    if obj < obj_minimo:
                        obj_minimo = obj
                    else:
                        pts(schedule,r,t1,t2)
    print('obj pts min test:',obj_minimo)