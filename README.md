# Processamento Distribuído de Logs com MPI

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MPI](https://img.shields.io/badge/MPI-mpi4py-000000?style=for-the-badge)](https://mpi4py.readthedocs.io/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)]()

Projeto desenvolvido para explorar o processamento distribuído de grandes volumes de logs utilizando a biblioteca `mpi4py` e a estratégia de comunicação `Scatter` do MPI.

## Visão Geral

Este projeto tem como objetivo demonstrar como dividir um conjunto de dados entre múltiplos processos em um ambiente de computação paralela, permitindo processamento mais eficiente em tarefas de análise de logs.

Ao invés de processar todos os registros em um único processo, os dados são distribuídos entre diferentes workers, que executam a análise em paralelo e retornam os resultados de forma organizada.

## Objetivo

- Aplicar conceitos de programação paralela e distribuída;
- Utilizar MPI para distribuir carga de trabalho;
- Processar grandes volumes de logs de forma escalável;
- Demonstrar uso prático do método `Scatter` do MPI;
- Criar um exemplo funcional, didático e apresentável em portfólio.

## Tecnologias Utilizadas

- Python 3
- MPI
- mpi4py
- Estrutura de paralelismo por processos
- Distribuição de dados via `Scatter`

## Como Funciona

A ideia principal do projeto é:

1. O processo mestre carrega o conjunto de logs;
2. Os dados são divididos em blocos menores;
3. Cada processo recebe uma parte do conjunto via `scatter`;
4. Cada worker processa sua fatia de dados;
5. Os resultados são agregados para formar a saída final.

Essa abordagem reduz o tempo de processamento e mostra um uso realista de paralelização em cenários de Big Data e análise de eventos.

## Estrutura do Projeto

```text
.
├── README.md
├── main.py
├── logs/
│   └── exemplo_logs.txt
├── requirements.txt
└── src/
    └── ...
```

## Requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.10 ou superior
- MPI instalado no sistema
- Biblioteca `mpi4py`

### Instalação

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

Se o arquivo `requirements.txt` ainda não existir, instale manualmente:

```bash
pip install mpi4py
```

## Execução

Para rodar o programa com múltiplos processos:

```bash
mpiexec -n 4 python main.py
```

Você pode alterar o número de processos conforme o ambiente e a quantidade de dados.

## Exemplo de Saída

```text
Processo 0: processou 250 logs
Processo 1: processou 250 logs
Processo 2: processou 250 logs
Processo 3: processou 250 logs

Total processado: 1000 logs
Análise concluída com sucesso.
```

## Casos de Uso

Este projeto pode ser expandido para aplicações como:

- Monitoramento de logs de servidores;
- Análise de eventos em tempo real;
- Processamento de registros de sistemas distribuídos;
- Diagnóstico de falhas e segurança;
- Pipeline de dados com processamento paralelo.

## Benefícios da Abordagem

- Redução do tempo de processamento;
- Melhor uso de múltiplos núcleos;
- Escalabilidade para grandes volumes de dados;
- Aplicação realista de paralelismo em Python;
- Demonstração técnica relevante para portfólio.

## Melhorias Futuras

- Implementar análise de erros e warnings por processo;
- Adicionar suporte para leitura de arquivos CSV ou JSON;
- Criar interface de linha de comando (CLI);
- Integrar relatórios mais detalhados de processamento;
- Comparar desempenho com execução sequencial.

## Conclusão

Este projeto demonstra uma aplicação prática de processamento distribuído usando MPI em Python. Além de reforçar conceitos importantes de computação paralela, ele também representa uma solução interessante para portfólio, especialmente para quem busca atuar em áreas como ciência de dados, sistemas distribuídos, engenharia de software e infraestrutura computacional.

## Autor

- Seu Nome

## Licença

Este projeto está disponível para fins acadêmicos e de estudo. Caso queira reutilizar ou adaptar o código, fique à vontade para modificar conforme sua necessidade.
