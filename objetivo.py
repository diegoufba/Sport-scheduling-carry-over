def objetivo(n,schedule,weight_table):
    carry_over_table = []
    for i in range (n):
        carry_over_table.append([0]*n)

    result = 0

    for teams in schedule:
        for i in range(n-2):
            t1 = teams[i]
            t2 = teams[i+1]
            carry_over_table[t1][t2] += 1
        carry_over_table[teams[n-2]][teams[0]] +=1

    for i in range(n):
        for j in range(n):
            result += weight_table[i][j] * (carry_over_table[i][j]**2)

    return result
