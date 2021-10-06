def prs(schedule,t,r1,r2):

    # schedule = [
    # [2,9,6,7,4,1,3,8,5],
    # [8,7,5,4,2,0,9,3,6],
    # [0,3,8,5,1,9,6,7,4],
    # [5,2,9,6,7,4,0,1,8],
    # [9,6,7,1,0,3,8,5,2],
    # [3,8,1,2,9,6,7,4,0],
    # [7,4,0,3,8,5,2,9,1],
    # [6,1,4,0,3,8,5,2,9],
    # [1,5,2,9,6,7,4,0,3],
    # [4,0,3,8,5,2,1,6,7]
    # ]

    initial_team = t
    for i in range (len(schedule)):
        
        # Troca de round dos times
        aux = schedule[t][r1]
        schedule[t][r1] = schedule[t][r2]
        schedule[t][r2] = aux

        if i % 2 != 0:
            t = schedule[t][r1]
        else:
            t = schedule[t][r2]
        if t == initial_team:
            #print(f'i: {i}')
            break

    return schedule