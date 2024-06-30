# Relatório Integrado de Implementação e Análise de Algoritmos Distribuídos Usando MPI4PY

## Introdução:
Este relatório compila a implementação e análise de três algoritmos distintos em um ambiente de computação distribuída usando a biblioteca `mpi4py`. Os algoritmos abordados incluem exclusão mútua distribuída, sincronização de relógios de Lamport e eleição de líder. Cada um desses algoritmos desempenha um papel crucial em sistemas distribuídos, garantindo a coordenação e a consistência entre processos paralelos.

## Descrição dos Problemas e Algoritmos:

1. **Exclusão Mútua Distribuída:**
   - **Objetivo:** Garantir que apenas um processo por vez acesse um recurso compartilhado em um ambiente de computação paralela.
   - **Algoritmo:** Variação do algoritmo de exclusão mútua distribuída, priorizando processos com menor valor de `prio`.

2. **Sincronização de Relógios de Lamport:**
   - **Objetivo:** Permitir que todos os processos em um sistema distribuído concordem sobre a ordem dos eventos sem um relógio global.
   - **Algoritmo:** Algoritmo de Lamport, que usa marcas de tempo para determinar a ordem dos eventos.

3. **Eleição de Líder:**
   - **Objetivo:** Eleger o nó com o maior valor como líder entre um conjunto de nós interconectados.
   - **Algoritmo:** Variação do algoritmo de eleição de líder, onde nós comunicam-se para identificar o líder com base no maior valor.

## Detalhes da Implementação:

- **Bibliotecas Utilizadas:**
  - `mpi4py`: Facilita a comunicação entre processos em sistemas distribuídos.
  - `time`: Usada para simular o tempo de ocupação do recurso.

- **Sistemas de Comunicação:**
  - Utilização de chamadas de MPI como `comm.send()`, `comm.recv()`, `comm.isend()`, `comm.irecv()`, e `comm.allgather()` para a comunicação entre processos.

- **Ambiente de Execução:**
  - Todos os códigos são destinados a serem executados em ambientes que suportem MPI, como clusters de computadores ou sistemas multicore.

## Resultados de Experimentos:

1. **Exclusão Mútua Distribuída:**
   - Apenas um processo por vez foi capaz de entrar na seção crítica, validado pelas mensagens de log.

2. **Sincronização de Relógios de Lamport:**
   - As marcas de tempo nos arquivos de saída confirmaram a correta atualização dos relógios de Lamport e a ordem dos eventos.

3. **Eleição de Líder:**
   - O nó com o maior valor foi consistentemente eleito como líder, com eficiência medida pelo número de mensagens trocadas e tempo de execução.

## Conclusão:
A implementação e análise dos algoritmos distribuídos usando `mpi4py` demonstraram a eficácia desta biblioteca em simular comportamentos complexos em sistemas distribuídos. Os experimentos realizados ajudaram a entender desafios como sincronização, comunicação entre processos e tratamento de condições de corrida.

## Referências

A única referência utilizada foi o tutorial de `mpi4py` presente em [https://mpi4py.readthedocs.io/en/stable/tutorial.html](https://mpi4py.readthedocs.io/en/stable/tutorial.html)
