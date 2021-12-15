from partial_team_swap.obj_pts import obj_pts,obj_pts2,objetivo
from readInstanceWeight import getInstance
from neighborhoods import pts_neighborhood
from saveSchedule import save_solution

schedule = [

    [2, 9, 3, 1, 6, 7, 8, 5, 4], 
    [5, 8, 2, 0, 7, 9, 4, 3, 6], #
    [0, 3, 1, 8, 5, 4, 9, 6, 7], 
    [9, 2, 0, 6, 4, 5, 7, 1, 8], 
    [6, 5, 7, 9, 3, 2, 1, 8, 0], #
    [1, 4, 8, 7, 2, 3, 6, 0, 9], 
    [4, 7, 9, 3, 0, 8, 5, 2, 1], 
    [8, 6, 4, 5, 1, 0, 3, 9, 2], 
    [7, 1, 5, 2, 9, 6, 0, 4, 3], 
    [3, 0, 6, 4, 8, 1, 2, 7, 5]

]

weight_table, n = getInstance(f'instances/inst{20}linearperturbacaoA.xml')
obj,carry_over_table = objetivo(schedule,weight_table)
#print(obj)

# s = {'schedule':schedule,'carry_over_table':carry_over_table,'obj':obj}

# print(pts_neighborhood(s,weight_table))
# save_solution(schedule)

r=0
t1=1
t2=3 #4
new_obj1, aux_carry_over_table1 = obj_pts(obj,schedule,r,t1,t2,weight_table,carry_over_table)
print(new_obj1)
print(aux_carry_over_table1)

new_obj2, aux_carry_over_table2 = obj_pts2(obj,schedule,r,t1,t2,weight_table,carry_over_table)
print(new_obj2)
print(aux_carry_over_table2)