# Projeto: Pipeline de Monitoramento de Sensores IoT - Kafka, Python, PostgreSQL & Docker

Este projeto implementa um pipeline de dados utilizando sensores IoT simulados, Kafka para mensageria, Python para processamento e PostgreSQL para armazenamento dos dados. Ele foi desenvolvido com Docker para facilitar a orquestração e a execução de todos os serviços envolvidos.


## Índice

1. [Estrutura do Projeto](#-estrutura-do-projeto)
2. [Fluxo do Pipeline](#fluxo-do-pipeline)
3. [Como Executar](#-como-executar)
    - [Clone o repositório](#1-clone-o-repositório)
    - [Suba os serviços com Docker](#2-suba-os-serviços-com-docker)
    - [Verifique os logs](#3-verifique-os-logs)
    - [Acesse o banco de dados (via terminal)](#4-acesse-o-banco-de-dados-via-terminal)
    - [Acesse o banco de dados (via Docker Desktop)](#4-acesse-o-banco-de-dados-via-docker-desktop)
    - [Reexecutar o projeto](#caso-deseje-reexecutar-o-projeto-use)
4. [Tecnologias Utilizadas](#️-tecnologias-utilizadas)
5. [Autor](#️autor)

---

## 📁 Estrutura do Projeto

- **docker-compose.yml**: Orquestra os serviços Kafka, Zookeeper, Producer, Consumer e PostgreSQL.
- **producer.py**: Simula sensores gerando dados aleatórios e envia para o Kafka.
- **consumer.py**: Consome mensagens do Kafka e armazena no PostgreSQL.
- **init.sql**: Script SQL que cria a tabela `sensores` no banco.
- **requirements.txt**: Dependências Python para rodar o producer e o consumer.

---

## Fluxo do Pipeline

1. **Producer**  
   Gera dados aleatórios de sensores (temperatura e umidade) com um `sensor_id` e `timestamp`.

2. **Kafka**  
   Recebe os dados e atua como intermediador de mensagens.

3. **Consumer**  
   Lê as mensagens do Kafka e insere os dados na tabela `sensores` do PostgreSQL.

4. **PostgreSQL**  
   Armazena os dados consumidos, permitindo consultas e análises futuras.

---

## 🚀 Como Executar

⚠️ **Atenção**: Este projeto depende do Docker. Certifique-se de instalar o [Docker Desktop](https://www.docker.com/products/docker-desktop/) antes de prosseguir.

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/iot-kafka-projeto.git
cd iot-kafka-projeto
```

### 2. Suba os serviços com Docker

```
docker-compose up --build
```

### 3. Verifique os logs
No terminal ou Docker Desktop, você verá:

No producer: mensagens Sent: {...} com os dados gerados.

No consumer: mensagens Received: {...} confirmando o consumo e inserção no banco.

### 4. Acesse o banco de dados (via terminal)

```
docker exec -it iot-kafka-projeto-db-1 psql -U user -d sensores
```

### 4. Acesse o banco de dados (via Docker Desktop)

Acesse o container > iot-kafka-projeto-db-1 > Exec

```
psql -U user -d sensores
```

Dentro do PostgreSQL via Docker Desktop ou terminal, você pode consultar os dados:

```sql
SELECT * FROM sensores ORDER BY id DESC LIMIT 5;
```

Caso deseje reexecutar o projeto, use:

```
docker-compose down
docker-compose up --build
```

## 🛠️ Tecnologias Utilizadas

- Python 3.10
- Apache Kafka
- PostgreSQL
- Docker & Docker Compose
- Kafka-Python

---

## Autor

Gabriel Soares Evangelista - [@gabrielsoaresevt](https://www.linkedin.com/in/gabriel-soares-evangelista)