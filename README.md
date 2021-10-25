# Sport-scheduling-carry-over
## 1. Leitura de Instância
O arquivo readInstanceWeight.py possui a função $getInstance(path)$ que tem como parâmetro o caminho da instância e como retorno o número de times ($n$) e a tabela de pesos do carry-over ($weight\_table$)
### Exemplo de uso
```
weight_table, n = getInstance('instances/inst6linearperturbacaoA.xml')
```
### Saída
```
n = 6  
weight_table = [  
    [2, 0, 1, 5, 1, 6]  
    [0, 1, 3, 0, 1, 4]  
    [3, 2, 0, 1, 4, 4]  
    [3, 3, 1, 1, 2, 4]  
    [3, 1, 0, 1, 1, 0]  
    [2, 2, 3, 1, 2, 2]  
]
```
### Para acessar o peso do carry-over que o time 2 dá no time 4
```
weight_table[2][4]
```
## 2. Método do Círculo
O arquivo circle.py possui a função $circle\_method(n)$ que tem como parâmetro o número de times ($n$) e retorno a tabela de jogos ($schedule$)

### Exemplo de uso:
```
schedule = circle_method(6)
```
### Saída
``` 
schedule = [  
    [5, 2, 4, 1, 3]
    [4, 5, 3, 0, 2]
    [3, 0, 5, 4, 1]
    [2, 4, 1, 5, 0]
    [1, 3, 0, 2, 5]
    [0, 1, 2, 3, 4]
]
```
### As linhas representam os times e as colunas as rodadas ,para acessar o oponente do time 1 na rodada 3
```
schedule[1][3]
```
## 3. Função Objetivo
O arquivo objetivo.py possui a função $objetivo(schedule,weight\_table)$ que tem como parâmetros a tabela de jogos ($schedule$) e a tabela de pesos do carry-over ($weight\_table$). Ela retorna o resultado da função objetivo ($result$)

### Exemplo de uso
```
obj = objetivo(schedule,weight_table)
```
### Saída
``` 
result = 118
```
## 4. Troca Parcial de Rodadas
O arquivo partial_round_swap.py possui a função $prs(schedule,t,r_1,r_2)$ que tem como parâmetro a tabela de jogos ($schedule$), o time que se deseja trocar de rodada ($t$) e os rounds ($r_1$ e $r_2$). Ela retorna uma nova tabela de jogos ($schedule$)

### Exemplo de uso
```
schedule = prs(schedule,0,1,3)
```
### Saída
``` 
schedule = [
    [5, 1, 4, 2, 3]
    [4, 0, 3, 5, 2]
    [3, 4, 5, 0, 1]
    [2, 5, 1, 4, 0]
    [1, 2, 0, 3, 5]
    [0, 3, 2, 1, 4]
]
```
## 5. Troca Parcial de Times
O arquivo partial_team_swap.py possui a função $pts(schedule,r,t_1,t_2)$ que tem como parâmetro a tabela de jogos ($schedule$), a rodada que se deseja trocar times ($r$) e os times ($t_1$ e $t_2$). Ela retorna uma nova tabela de jogos ($schedule$)

### Exemplo de uso
```
schedule = pts(schedule,1,0,1)
```
### Saída
``` 
schedule = [
    [4, 5, 3, 1, 2]
    [5, 2, 4, 0, 3]
    [3, 1, 5, 4, 0]
    [2, 4, 0, 5, 1]
    [0, 3, 1, 2, 5]
    [1, 0, 2, 3, 4]
]
```
## 6. Salva resultado em XML
O arquivo saveSchedule.py possui a função $save\_solution(schedule)$ que tem como parâmetro a tabela de jogos ($schedule$) e gera como resultado o arquivo *Solution.xml* que pode ser valido no site https://www.sportscheduling.ugent.be/RobinX/ 

### Exemplo de uso
```
save_solution(schedule)
```
### Saída
```
<?xml version="1.0" ?>
<Solution>
   <Games>
      <ScheduledMatch home="0" away="4" slot="0"/>
      <ScheduledMatch home="0" away="5" slot="1"/>
      <ScheduledMatch home="0" away="3" slot="2"/>
      <ScheduledMatch home="0" away="1" slot="3"/>
      <ScheduledMatch home="0" away="2" slot="4"/>
      <ScheduledMatch home="1" away="5" slot="0"/>
      <ScheduledMatch home="1" away="2" slot="1"/>
      <ScheduledMatch home="1" away="4" slot="2"/>
      <ScheduledMatch home="1" away="3" slot="4"/>
      <ScheduledMatch home="2" away="3" slot="0"/>
      <ScheduledMatch home="2" away="5" slot="2"/>
      <ScheduledMatch home="2" away="4" slot="3"/>
      <ScheduledMatch home="3" away="4" slot="1"/>
      <ScheduledMatch home="3" away="5" slot="3"/>
      <ScheduledMatch home="4" away="5" slot="4"/>
   </Games>
</Solution>

```