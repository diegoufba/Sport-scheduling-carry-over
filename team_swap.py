def ts(schedule,t1,t2):
    # Troca as linhas
    schedule[t1], schedule[t2] = schedule[t2], schedule[t1]

    # Troca os times no restante da tabela
    for i,teams in enumerate(schedule):
        if i == t1:
            pos_t1 = teams.index(t1)
            teams[pos_t1] = t2
        if i == t2:
            pos_t2 = teams.index(t2)
            teams[pos_t2] = t1
        if i!= t1 and i!=t2:
            pos_t1 = teams.index(t1)
            pos_t2 = teams.index(t2)
            teams[pos_t1],teams[pos_t2] = teams[pos_t2],teams[pos_t1] 
    return schedule