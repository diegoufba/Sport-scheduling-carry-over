#import matplotlib.pyplot as plt
import math
import time
from c_profile import profile
import random
from geradores.circle import circle_method
from objetivo import objetivo
from geradores.vizing_professor import vizing
#from copy import deepcopy
from neighborhoods import ts_neighborhood,rs_neighborhood, prs_neighborhood, pts_neighborhood

from partial_round_swap.prs import prs
from partial_team_swap.pts import pts

from readInstanceWeight import getInstance
from saveSchedule import save_solution

def copy(sol):
    schedule_copy = [x[:] for x in sol['schedule']]
    carry_over_table_copy = [x[:] for x in sol['carry_over_table']]
    obj_copy = sol['obj']
    sol_copy = {'schedule':schedule_copy,'carry_over_table':carry_over_table_copy,'obj':obj_copy}
    return sol_copy

def pertubacao(s,weight_table):
    n = len(weight_table)

    n_movements = random.randint(3,4)

    for i in range (n_movements):
        movement = random.randint(0,1)
        if movement == 0:
            t = random.randint(0,n-1)
            r1,r2 = random.sample(range(n-1),2)
            prs(s['schedule'],t,r1,r2)
        else:
            r = random.randint(0,n-2)
            t1,t2 = random.sample(range(n),2)

            # t1 e t2 nao podem se enfrentar na rodada r
            if s['schedule'][t1][r] != t2:
                pts(s['schedule'],r,t1,t2)
    
    s['obj'],s['carry_over_table'] = objetivo(s['schedule'],weight_table)


def RVND(s,weight_table):
    s_rvnd = copy(s)
    #neighborhood_list = [ts_neighborhood,rs_neighborhood,prs_neighborhood,pts_neighborhood]
    neighborhood_list = [ts_neighborhood,rs_neighborhood,prs_neighborhood]
    #neighborhood_list = [pts_neighborhood]

    while neighborhood_list:
        choosen_neighborhood =  random.choice(neighborhood_list)
        choosen_neighborhood(s_rvnd,weight_table)

        if s_rvnd['obj'] < s['obj']:
            s = copy(s_rvnd)
            #neighborhood_list = [ts_neighborhood,rs_neighborhood,prs_neighborhood,pts_neighborhood]
            neighborhood_list = [ts_neighborhood,rs_neighborhood,prs_neighborhood]
            #neighborhood_list = [pts_neighborhood]
        else:
            neighborhood_list.remove(choosen_neighborhood)

    return s

#@profile
def local_search(Imax,Iils,weight_table,n):

    # schedule = vizing(n-1)
    # obj,carry_over_table = objetivo(schedule,weight_table)
    # s_star = {'schedule':schedule,'carry_over_table':carry_over_table,'obj':obj}

    s_star = {'obj':math.inf}
    for i in range(Imax):
        # Gera solucao inicial por Vizing
        schedule = vizing(n-1)
        obj,carry_over_table = objetivo(schedule,weight_table)
        s = {'schedule':schedule,'carry_over_table':carry_over_table,'obj':obj}
        
        s_linha = copy(s)
        iterILS = 0

        while iterILS < Iils:
            s = RVND(s,weight_table)
            
            if s['obj'] < s_linha['obj']:
                s_linha = copy(s)
                iterILS = 0
            s = copy(s_linha)

            pertubacao(s,weight_table)

            iterILS = iterILS + 1

            time_linha.write(f'{time.time() - start_time}\n')
            obj_linha.write(f"{s_linha['obj']}\n")
            #time_linha.append(time.time() - start_time)
            #obj_linha.append(s_linha['obj'])

        #print(s_star['obj'])
        if s_linha['obj'] < s_star['obj']:
            s_star = copy(s_linha)
        
        time_star.write(f'{time.time() - start_time}\n')
        obj_star.write(f"{s_star['obj']}\n")
        #time_star.append(time.time() - start_time)
        #obj_star.append(s_star['obj'])
        

    return s_star

# 10 - 315
#random.seed(10)
time_linha = open('time_linha.txt', 'w+')
time_star = open('time_star.txt', 'w+')
obj_linha = open('obj_linha.txt', 'w+')
obj_star = open('obj_star.txt', 'w+')

weight_table, n = getInstance(f'instances/inst{10}linearperturbacaoA.xml')
#schedule = vizing(n-1)
#print(schedule)
#schedule = circle_method(n)
#obj,carry_over_table = objetivo(schedule,weight_table)

#print(obj)

#s = {'schedule':schedule,'carry_over_table':carry_over_table,'obj':obj}
#s = RVND(s,weight_table)

start_time = time.time()
# time_linha = []
# obj_linha = []
# time_star = []
# obj_star = []

s = local_search(20,20,weight_table,n)
save_solution(s['schedule'])

print(s['obj'])
# plt.plot(time_linha,obj_linha)
# plt.plot(time_star,obj_star)
# plt.xlabel('tempo')
# plt.ylabel('objetivo')
# plt.show()

time_linha.close()
time_star.close()
obj_linha.close()
obj_star.close()