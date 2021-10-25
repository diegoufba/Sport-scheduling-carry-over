import random
from circle import circle_method
from objetivo import objetivo
from readInstanceWeight import getInstance

# Ler a instancia
weight_table, n = getInstance('instances/inst6linearperturbacaoA.xml')

# Gera a solucao pelo metodo do circulo
schedule = circle_method(n)

print('obj1:',objetivo(schedule,weight_table))

def nearest_neighbor(new_schedule,schedule,weight_table,free_rounds):
    #print('obj2:',objetivo(new_schedule,weight_table))
    new_round = random.choice(free_rounds)
    return new_round

def improve_initial_solution(schedule,weight_table):
    n = len(schedule)

    new_schedule = []
    
    free_rounds = list(range(n-1))

    # Escolhe dois rounds aleatorios para a nova solucao
    r1,r2 = random.sample(range(n-1),2)
    free_rounds.remove(r1)
    free_rounds.remove(r2)

    for line in schedule:
        new_schedule.append([line[r1],line[r2]])

    n_free_rounds = len(free_rounds)
    
    for i in range(2,n_free_rounds+2):
        new_round = nearest_neighbor(new_schedule,schedule,weight_table,free_rounds)
        free_rounds.remove(new_round)
        for j,line in enumerate(schedule):
            new_schedule[j].append(line[new_round])
    
    for line in new_schedule:
        print(line)
    print('obj2:',objetivo(new_schedule,weight_table))

improve_initial_solution(schedule,weight_table)