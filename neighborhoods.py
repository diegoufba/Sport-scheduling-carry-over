#from obj_pts import obj_pts
from team_swap.ts import ts
from team_swap.obj_ts import obj_ts
from round_swap.rs import rs
from round_swap.obj_rs import obj_rs
from partial_round_swap.prs import prs
from partial_round_swap.obj_prs import obj_prs
from partial_team_swap.pts import pts
from partial_team_swap.obj_pts import obj_pts


def ts_neighborhood(s,weight_table):
    obj_minimo = s['obj']
    obj_inicial = s['obj']
    n = len(s['schedule'])

    for t1 in range(n-1):
        for t2 in range(t1+1,n):
            obj,c = obj_ts(obj_inicial,s['schedule'],t1,t2,weight_table,s['carry_over_table'])
            if obj < obj_minimo:
                obj_minimo = obj
                best_t1 = t1
                best_t2 = t2
                best_carry_over_table = c

    if obj_minimo < obj_inicial:
        ts(s['schedule'],best_t1,best_t2)
        s['carry_over_table'] = best_carry_over_table
        s['obj'] = obj_minimo

    return s
    #print('obj ts min:',obj_minimo)

def rs_neighborhood(s,weight_table):
    obj_minimo = s['obj']
    obj_inicial = s['obj']
    n = len(s['schedule'])

    for r1 in range(n-2):
        for r2 in range(r1+1,n-1):
            obj,c = obj_rs(obj_inicial,s['schedule'],r1,r2,weight_table,s['carry_over_table'])
            if obj < obj_minimo:
                obj_minimo = obj
                best_r1 = r1
                best_r2 = r2
                best_carry_over_table = c

    if obj_minimo < obj_inicial:
        rs(s['schedule'],best_r1,best_r2)
        s['carry_over_table'] = best_carry_over_table
        s['obj'] = obj_minimo

    return s
    #print('obj rs min:',obj_minimo)

def prs_neighborhood(s,weight_table):
    obj_minimo = s['obj']
    obj_inicial = s['obj']
    n = len(s['schedule'])

    for r1 in range(n-2):
        for r2 in range(r1+1,n-1):
            for t in range(n):
                obj,c = obj_prs(obj_inicial,s['schedule'],t,r1,r2,weight_table,s['carry_over_table'])
                if obj < obj_minimo:
                    obj_minimo = obj
                    best_r1 = r1
                    best_r2 = r2
                    best_t = t
                    best_carry_over_table = c

    if obj_minimo < obj_inicial:
        prs(s['schedule'],best_t,best_r1,best_r2)
        s['carry_over_table'] = best_carry_over_table
        s['obj'] = obj_minimo
            
    return s
    #print('obj prs min:',obj_minimo)

def pts_neighborhood(s,weight_table):
    obj_minimo = s['obj']
    obj_inicial = s['obj']
    n = len(s['schedule'])

    for t1 in range(n-1):
        for t2 in range(t1+1,n):
            for r in range(n-1):
                if s['schedule'][t1][r] == t2:
                    continue
                obj,c = obj_pts(obj_inicial,s['schedule'],r,t1,t2,weight_table,s['carry_over_table'])
                if obj < obj_minimo:
                    obj_minimo = obj
                    best_t1 = t1
                    best_t2 = t2
                    best_r = r
                    best_carry_over_table = c

    if obj_minimo < obj_inicial:
        #print(obj_inicial,best_r,best_t1,best_t2)
        pts(s['schedule'],best_r,best_t1,best_t2)
        s['carry_over_table'] = best_carry_over_table
        s['obj'] = obj_minimo

    #print(s['obj'])
    return s
    #print('obj ts min:',obj_minimo)