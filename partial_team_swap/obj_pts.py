from circle import circle_method

#(obj,schedule,r,t1,t2,weight_table,carry_over_table)
def obj_pts(schedule,r,t1,t2):
    initial_round = r
    rounds = [r]
    for i in range (len(schedule)-1):
        next_r = schedule[t1].index(schedule[t2][r])

        if next_r == initial_round:
            break
        else:
            r = next_r
            rounds.append(r)
    if len(rounds) == len(schedule):
        pass
    rounds.sort()
    print(rounds)

schedule = circle_method(10)
obj = obj_pts(schedule,1,0,1)