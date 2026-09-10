# Processamento Distribuído de Logs com MPI

**Aluno:** Pedro Roberto Fernandes Noronha 
**Matrícula:**  10443434


---

## 1. Objetivo

O objetivo era gerar uma lista de logs, dividir entre processos igualmente atraves so scatter, processar e buscar erros.

## 2. Ambiente de Execução

| Item | Valor |
|---|---|
| Sistema operacional | Linux |
| Versão do Python | Python 3.12.1 |
| Núcleos disponíveis | 2 |
| Nº de processos usados | 4 |
| Total de logs | 100.000 |

## 3. Implementação

### Etapa 1 — Geração do dataset
Laço de qtd iterações, ramdom sorteia um item de cada lista e ao final e formatada uma string, o append acumula os logs.


### Etapa 2 — Divisão dos dados
calcula quanto cada processo recebe, e fatia a lista de logs.

### Etapa 3 — Distribuição com Scatter
O Rank 0 entrega o item 0 por 0, o 1 para o rank 1, cada processo guarda o que recebeu em logs locais.

### Etapa 4 — Processamento local
Faz um split, seleciona o indice que corresponde aos codigos de erro e faz a contagem.

### Etapa 5 — Envio ao master
Todos montam a mensagem já formatada. Os workers caem no else e mandam a string pro master com send(..., dest=0). O master imprime a própria primeiro e depois roda range(1, size), chamando recv(source=origem) uma vez por worker.

## 4. Resultados

**Comando executado:**

```bash
mpirun --oversubscribe -np 4 python logs_scatter.py
```

**Saída obtida:**

```
![alt text](<Captura de tela 2026-09-10 200617.png>)
```

| Processo | Linhas | Erros | % de erros |
|---|---|---|---|
| 0 | 25000 | 9973 | 39,89% |
| 1 | 25000 | 10055 | 40,22% |
| 2 | 25000 | 9827 | 39,31% |
| 3 | 25000 | 10002 | 40,01% |
| **Total** | **100000** | **39857** | **39,86%** |

## 5. Discussão

- **Proporção de erros:** A proporção de erros ficou proximo aos 40%, por uma questão matematica.Fizemos uma distribuição uniforme onde a proporção de erros era de 2 para 5.
- **Divisão inteira:** O cálculo `TOTAL_LOGS // size` usa divisão inteira e descarta o
  resto. Com 100.000 linhas e 4 processos a divisão é exata (25.000 cada), mas com 3
  processos cada um receberia 33.333 linhas e uma linha ficaria de fora do processamento.
- **Oversubscribe:** na primeira tentativa de execução o OpenMPI retornou o erro "not
  enough slots available", pois o ambiente utilizado dispõe de menos núcleos do que os
  4 processos solicitados. Por padrão o OpenMPI recusa lançar mais processos do que
  núcleos físicos. A flag `--oversubscribe` desativa essa verificação, permitindo que os
  processos compartilhem os núcleos disponíveis.
- **Coletiva vs. ponto a ponto:** o Scatter é uma operação coletiva,precisa ser chamada
  por todos os processos, distribui os dados em uma única instrução e sincroniza a
  execução, já que ninguém prossegue antes de todos receberem sua fatia. Já o `send`/`recv` da Etapa 5 é ponto a ponto: cada worker envia individualmente ao master, que executa um `recv` por origem.

## 6. Conclusão

A atividade demonstrou na prática o particionamento e a distribuição de dados em um
ambiente de memória distribuída, no qual cada processo opera sobre sua própria fatia
sem acesso à memória dos demais. O uso do Scatter evidenciou que a estrutura dos dados
precisa ser preparada previamente pelo processo raiz e que operações coletivas exigem participação de todos os ranks.

