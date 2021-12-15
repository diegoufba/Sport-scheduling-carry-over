import cProfile
import sys
from local_search import local_search
from readInstanceWeight import getInstance
from saveSchedule import save_solution

#@profile
def main():
    # Tamanho da instancia disponiveis: 6,10,12,14,16,18,20
    # Exemplo de execucao: pypy main.py 10 50 100
    instance_size,Imax,Iils = sys.argv[1:]

    # Ler a instancia
    weight_table, n = getInstance(f'instances/inst{instance_size}linearperturbacaoA.xml')

    #random.seed(10)
    s = local_search(int(Imax),int(Iils),weight_table,n)

    save_solution(s['schedule'])

    print(s['obj'])

if __name__ == "__main__":
    main()