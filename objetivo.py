from circle import circle_method
from readInstance import getInstance

myInstance = getInstance('inst4linearperturbacaoA')
n = 8
schedule = circle_method(n)
carry_over_table = []
for i in range (n):
    carry_over_table.append([0]*n)

schedule = [
    [7,2,3,4,5,6,1],
    [2,3,4,5,6,7,0],
    [1,0,5,7,4,3,6],
    [4,1,0,6,7,2,5],
    [3,6,1,0,2,5,7],
    [6,7,2,1,0,4,3],
    [5,4,7,3,1,0,2],
    [0,5,6,2,3,1,4]
]

for teams in schedule:
    for i in range(n-2):
        t1 = teams[i]
        t2 = teams[i+1]
        carry_over_table[t1][t2] += 1
    carry_over_table[teams[n-2]][teams[0]] +=1

print(carry_over_table)
