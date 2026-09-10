from mpi4py import MPI
import random

# Inicialização do MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


#
# Função para gerar logs
#
def gerar_logs(qtd):
    ips = [f"192.168.1.{i}" for i in range(2, 254)]
    endpoints = [
        "/",
        "/login",
        "/products",
        "/cart",
        "/checkout",
        "/api/users",
        "/api/orders"
    ]
    metodos = ["GET", "POST"]
    status = ["200", "200", "200", "404", "500"]

    logs = []
    # INSIRA AQUI O SEU CÓDIGO PARA GERAR OS DADOS DO LOG
    # RANDOMIZE OS IPS, ENDPOINTS, METODOS E STATUS
    # Vamos pegar um aleatorio da lista, rodar no loop e montar

    for _ in range(qtd):
        ip = random.choice(ips)
        metodo = random.choice(metodos)
        endpoint = random.choice(endpoints)
        st = random.choice(status)
        logs.append(f"{ip} {metodo} {endpoint} {st}")

    return logs

    


#
# Processo 0 gera o dataset
#
logs_divididos = None
TOTAL_LOGS = 100000

if rank == 0:
    print("\nGerando dataset de logs...\n")
    logs = gerar_logs(TOTAL_LOGS)

    # DIVIDIR AQUI O DATASET ENTRE OS PROCESSOS
    # O NÓ MASTER TAMBÉM PROCESSA SUA PARTE DO DATASET

    tamanho_fatia = TOTAL_LOGS // size

    logs_divididos = []
    for i in range(size):
        inicio = i * tamanho_fatia
        fim = inicio + tamanho_fatia
        logs_divididos.append(logs[inicio:fim])

#
# Distribuição usando Scatter
#
# DISTRIBUIR OS DADOS USANDO SCATTER
logs_locais = comm.scatter(logs_divididos, root=0)

#
# Processamento local em cada nó
#
# INSIRA AQUI O CÓDIGO DE PROCESSAMENTO LOCAL DO LOG
erros = 0

for linha in logs_locais:
    campos = linha.split()
    status = campos[3]
    if status in ("404", "500"):
        erros += 1

#
# Nós Master
# Imprime os resultados de cada nó worker e seu também
#
# A variável 'logs_locais' representa a fatia recebida e 'erros' o contador
#print(f"Processo {rank} analisou {len(logs_locais)} linhas "
#     f"e encontrou {erros} erros."
#)

mensagem = (
    f"Processo {rank} analisou {len(logs_locais)} linhas "
    f"e encontrou {erros} erros."
)
if rank == 0:
    print(mensagem)
    for origem in range(1, size):
        print(comm.recv(source=origem))
else:
    comm.send(mensagem, dest=0)