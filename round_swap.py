def rs(schedule,r1,r2):
    for i in range (len(schedule)):
        # Troca de round
        schedule[i][r1] ,schedule[i][r2] = schedule[i][r2] ,schedule[i][r1]