from circle import circle_method
from objetivo import objetivo
from readInstanceWeight import getInstance
from saveSchedule import save_solution
from round_swap import rs

def min_rs():
    # Round Swap para Objetivo Minimo
    # Ler a instancia
    weight_table, n = getInstance('instances/inst10linearperturbacaoA.xml')

    # Gera a solucao pelo metodo do circulo
    schedule = circle_method(n)

    obj,carry_over_table = objetivo(schedule,weight_table)
    obj_minimo = obj
    for r1 in range(n-2):
        for r2 in range(n-2):
            if r1 < r2:
                rs(schedule,r1,r2)
                obj,carry_over_table = objetivo(schedule,weight_table)
                if obj < obj_minimo:
                    obj_minimo = obj
                else:
                    rs(schedule,r1,r2)
    print(obj_minimo)
    save_solution(schedule)

min_rs()