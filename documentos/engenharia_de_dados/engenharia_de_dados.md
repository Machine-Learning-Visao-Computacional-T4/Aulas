# Fundamentos de Engenharia de Dados

## Sumário

- [1. Fontes de dados](#1-fontes-de-dados)
  - [Dados fornecidos pelos usuários](#dados-fornecidos-pelos-usuários)
  - [Dados gerados pelo sistema](#dados-gerados-pelo-sistema)
  - [Bancos de dados internos](#bancos-de-dados-internos)
  - [Dados externos](#dados-externos)
- [2. Formatos de dados](#2-formatos-de-dados)
  - [Serialização](#serialização)
  - [JSON](#json)
  - [CSV e Parquet](#csv-e-parquet)
  - [Texto versus binário](#texto-versus-binário)
- [3. Modelos de dados](#3-modelos-de-dados)
  - [Modelo relacional](#modelo-relacional)
  - [SQL declarativo](#sql-declarativo)
  - [Modelo de documentos](#modelo-de-documentos)
  - [Modelo de grafos](#modelo-de-grafos)
- [4. Dados estruturados e não estruturados](#4-dados-estruturados-e-não-estruturados)
  - [Dados estruturados](#dados-estruturados)
  - [Dados não estruturados](#dados-não-estruturados)
  - [Data warehouse e data lake](#data-warehouse-e-data-lake)
- [5. Processamento transacional e analítico](#5-processamento-transacional-e-analítico)
  - [OLTP — processamento transacional](#oltp--processamento-transacional)
  - [OLAP — processamento analítico](#olap--processamento-analítico)
- [6. ETL e ELT](#6-etl-e-elt)
  - [ETL — Extract, Transform, Load](#etl--extract-transform-load)
  - [ELT — Extract, Load, Transform](#elt--extract-load-transform)
- [7. Como os dados circulam entre sistemas](#7-como-os-dados-circulam-entre-sistemas)
  - [Por meio de bancos de dados](#por-meio-de-bancos-de-dados)
  - [Por meio de APIs](#por-meio-de-apis)
  - [Por meio de eventos e filas](#por-meio-de-eventos-e-filas)
- [8. Processamento batch e streaming](#8-processamento-batch-e-streaming)
  - [Batch](#batch)
  - [Streaming](#streaming)
- [Síntese final](#síntese-final)

## 1. Fontes de dados

Um sistema de ML pode receber dados de diferentes fontes, e cada uma exige cuidados específicos.

### Dados fornecidos pelos usuários

São informações inseridas diretamente pelas pessoas, como textos, formulários, imagens, vídeos ou arquivos.

Esses dados precisam de **validação** porque podem chegar incompletos, incorretos ou no formato errado.

> **Exemplo:** em um formulário que solicita a renda mensal, o usuário pode escrever "não sei" em um campo que deveria receber um número.

Além disso, normalmente o usuário espera uma resposta rápida. Se um formulário chama um agente de IA, por exemplo, o processamento não pode demorar vários minutos.

### Dados gerados pelo sistema

São produzidos automaticamente pelas aplicações, como:

- logs de execução;
- erros;
- uso de memória;
- chamadas de APIs;
- predições de modelos;
- tempo de resposta;
- comportamento dos usuários.

> **Exemplo:** uma API de *guardrails* pode registrar que uma requisição foi rejeitada por tentativa de *prompt injection*, sem armazenar o conteúdo sensível da mensagem.

Os logs são importantes para monitoramento e investigação de problemas, mas crescem rapidamente. Por isso, é necessário definir:

- por quanto tempo serão armazenados;
- quais eventos realmente precisam ser registrados;
- quais logs podem ser movidos para um armazenamento mais barato;
- como encontrar informações importantes no meio de tanto volume.

Mesmo sendo gerados pelo sistema, dados sobre cliques, navegação e comportamento continuam sendo dados de usuários e podem estar sujeitos a regras de privacidade.

### Bancos de dados internos

São dados produzidos pelos sistemas e áreas da própria organização, como CRM, inventário, cadastro de usuários e gestão de casos.

> **Exemplo:** um modelo pode recomendar um recurso para uma família, mas antes de mostrar a recomendação precisa consultar um banco interno para verificar se o recurso ainda está disponível.

### Dados externos

Podem ser classificados como:

- **First-party data:** coletados diretamente pela própria organização;
- **Second-party data:** coletados por outra organização sobre seus próprios usuários e compartilhados com você;
- **Third-party data:** coletados por empresas especializadas a partir de diversas fontes externas.

> **Exemplo:** uma organização pode combinar seus próprios dados de atendimento com informações públicas de localização e serviços comunitários.

Dados externos exigem atenção à qualidade, à licença de uso, à privacidade e à procedência.

## 2. Formatos de dados

Depois de coletados, os dados precisam ser armazenados em algum formato. A escolha influencia o custo, a velocidade e a facilidade de processamento.

### Serialização

**Serialização** é o processo de transformar um objeto ou estrutura em um formato que possa ser armazenado ou transmitido e depois reconstruído.

Alguns formatos comuns:

| Formato | Tipo | Legível por humanos | Uso comum |
| --- | --- | --- | --- |
| JSON | Texto | Sim | APIs e configurações |
| CSV | Texto | Sim | Tabelas e intercâmbio de dados |
| Parquet | Binário | Não | Data lakes e análises em grande escala |
| Avro | Binário | Não | Hadoop e transmissão de dados |
| Protobuf | Binário | Não | Comunicação entre serviços |
| Pickle | Binário | Não | Objetos Python |

### JSON

O JSON representa dados usando pares de chave e valor e aceita estruturas aninhadas.

Exemplo:

```json
{
  "name": "Maria",
  "age": 42,
  "state": "US-TX",
  "needs": ["housing", "food"]
}
```

É muito utilizado em APIs porque é legível e funciona em diferentes linguagens. Entretanto, ocupa mais espaço que formatos binários e mudanças de estrutura podem quebrar aplicações que esperam um esquema específico.

### CSV e Parquet

A principal diferença está na forma como os dados são organizados:

- **CSV:** orientação por linhas;
- **Parquet:** orientação por colunas.

Considere uma tabela com mil colunas. Se uma análise utiliza somente `state`, `income`, `primary_need` e `created_at`, o Parquet consegue ler apenas essas quatro colunas. Em CSV, geralmente é necessário ler a linha inteira e depois selecionar os campos desejados.

Por isso:

- formatos orientados por **linhas** são bons para inserir ou recuperar registros completos;
- formatos orientados por **colunas** são melhores para análises, agregações e leitura de poucas colunas em tabelas grandes.

> **Exemplo:** para registrar uma nova solicitação individual, a organização por linha é conveniente. Para calcular a renda média por estado em milhões de solicitações, a organização por coluna é mais eficiente.

### Texto versus binário

JSON e CSV são formatos de texto. Parquet, Avro e Protobuf são formatos binários.

**Formatos de texto:**

- são fáceis de abrir e ler;
- facilitam inspeções manuais;
- geralmente ocupam mais espaço;
- podem ser mais lentos para grandes volumes.

**Formatos binários:**

- são mais compactos;
- geralmente oferecem melhor desempenho;
- precisam de um programa que saiba interpretá-los;
- não são diretamente legíveis por pessoas.

No exemplo apresentado no capítulo, um arquivo CSV de 14 MB passou a ocupar 6 MB ao ser convertido para Parquet.

## 3. Modelos de dados

O **formato** define como os dados são codificados. O **modelo de dados** define como eles são representados e relacionados.

Um carro, por exemplo, pode ser representado por:

- marca, modelo, ano, cor e preço; ou
- proprietário, placa e histórico de endereços.

O primeiro modelo é útil para vendas. O segundo é mais apropriado para rastreamento e investigação. Portanto, a representação escolhida influencia diretamente quais problemas serão fáceis ou difíceis de resolver.

### Modelo relacional

Organiza os dados em tabelas formadas por linhas e colunas. As tabelas podem ser relacionadas por identificadores.

Exemplo:

**Tabela `books`**

| title | publisher_id | price |
| --- | --- | --- |
| Harry Potter | 1 | 20 |
| The Hobbit | 1 | 30 |

**Tabela `publishers`**

| publisher_id | name | country |
| --- | --- | --- |
| 1 | Banana Press | UK |

Essa separação é chamada de **normalização**. Ela reduz duplicidade e melhora a consistência.

Se a editora mudar de nome, atualizamos apenas um registro na tabela `publishers`, em vez de modificar todos os livros associados a ela.

A desvantagem é que recuperar a informação completa pode exigir vários `JOIN`s, que podem ser caros em grandes volumes.

### SQL declarativo

SQL é uma linguagem **declarativa**: informamos o resultado desejado, e o banco decide como executar a operação.

```sql
SELECT state, COUNT(*) AS total_requests
FROM support_cases
GROUP BY state;
```

A consulta diz *o que* queremos, mas não descreve todas as etapas internas de leitura, distribuição e agregação. O otimizador do banco escolhe o plano de execução.

Em Python, normalmente usamos uma abordagem mais **imperativa**, descrevendo os passos que o computador deverá executar.

### Modelo de documentos

Armazena cada entidade como um documento, normalmente em JSON ou BSON.

```json
{
  "title": "Harry Potter",
  "publisher": {
    "name": "Banana Press",
    "country": "UK"
  },
  "formats": [
    {"type": "paperback", "price": 20},
    {"type": "ebook", "price": 10}
  ]
}
```

A vantagem é a **localidade**: todas as informações do livro estão no mesmo documento, sem necessidade de consultar várias tabelas.

Também existe mais flexibilidade, pois documentos da mesma coleção podem ter campos diferentes. Porém, dizer que o sistema é "sem esquema" não é completamente correto. A estrutura continua existindo; a responsabilidade de interpretá-la foi transferida para a aplicação que lê os dados.

Consultas e relacionamentos entre muitos documentos também podem ser mais difíceis.

### Modelo de grafos

Representa os dados por meio de:

- **Nós:** pessoas, cidades, empresas ou recursos;
- **Arestas:** relações entre esses elementos.

Exemplo:

```text
Pessoa → mora em → Curitiba
Pessoa → trabalha em → Empresa
Pessoa → conhece → Outra pessoa
```

Grafos são adequados quando as **relações** são mais importantes que o conteúdo isolado.

> **Exemplo:** encontrar recursos utilizados por pessoas semelhantes, conexões entre famílias e serviços ou caminhos entre organizações de uma rede comunitária.

## 4. Dados estruturados e não estruturados

### Dados estruturados

Seguem um esquema predefinido.

Exemplo:

| name | age | state |
| --- | --- | --- |
| Ana | 38 | PR |

Como sabemos que `age` é numérico, podemos calcular facilmente a média das idades.

O problema aparece quando o esquema muda. Se antes não existia o campo `email`, os registros antigos precisarão ser atualizados ou tratados como nulos.

Também é preciso tomar cuidado com valores ausentes. Substituir uma idade desconhecida por `0`, por exemplo, pode levar um modelo a interpretar que a pessoa tem zero anos.

### Dados não estruturados

Não precisam seguir um esquema rígido. Podem incluir:

- textos livres;
- imagens;
- áudios;
- vídeos;
- documentos;
- logs.

> **Exemplo:** a narrativa escrita por uma família explicando sua situação não possui as mesmas colunas fixas de uma tabela, embora um modelo de NLP possa extrair dela necessidades, riscos e sentimentos.

### Data warehouse e data lake

- **Data warehouse:** normalmente armazena dados estruturados e preparados para análise;
- **Data lake:** normalmente armazena dados brutos, estruturados ou não estruturados;
- **Lakehouse:** combina a flexibilidade do data lake com mecanismos de qualidade, governança e consulta típicos de um warehouse.

No modelo **Bronze–Silver–Gold**:

| Camada | Conteúdo |
| --- | --- |
| **Bronze** | Dados próximos da forma original |
| **Silver** | Dados limpos, validados e padronizados |
| **Gold** | Dados agregados e preparados para consumo, relatórios ou ML |

## 5. Processamento transacional e analítico

### OLTP — processamento transacional

É otimizado para operações rápidas e individuais, como:

- criar uma solicitação;
- atualizar um cadastro;
- registrar um pagamento;
- enviar um formulário.

Esses sistemas precisam de baixa latência e alta disponibilidade.

Um conceito associado é o **ACID**:

- **Atomicidade:** ou toda a transação funciona, ou nada é aplicado;
- **Consistência:** a transação respeita as regras do sistema;
- **Isolamento:** transações simultâneas não interferem indevidamente;
- **Durabilidade:** depois de confirmada, a alteração não é perdida.

> **Exemplo:** ao reservar um recurso, o sistema não pode confirmar a reserva para duas pessoas ao mesmo tempo.

### OLAP — processamento analítico

É otimizado para analisar muitas linhas e realizar agregações.

Exemplo:

> Qual foi o tempo médio de resolução dos casos por estado nos últimos 12 meses?

Essa consulta percorre muitos registros e agrupa valores, sendo diferente de simplesmente criar ou atualizar um caso.

Atualmente, a separação entre OLTP e OLAP está menos rígida. Algumas tecnologias conseguem executar os dois tipos de carga, e muitas arquiteturas separam armazenamento e computação.

## 6. ETL e ELT

### ETL — Extract, Transform, Load

- **Extract:** extrair dados das fontes;
- **Transform:** limpar, padronizar, combinar e validar;
- **Load:** carregar o resultado no destino.

Exemplo:

1. Extrair casos do ConnectMe;
2. Padronizar estados, remover duplicidades e abrir campos aninhados;
3. Carregar o resultado em uma tabela Silver no Databricks.

Na transformação, podemos:

- corrigir tipos;
- padronizar valores;
- fazer joins;
- remover duplicidades;
- criar features;
- agregar dados;
- validar regras de qualidade.

### ELT — Extract, Load, Transform

No ELT, os dados são primeiro carregados em um data lake e transformados posteriormente.

Exemplo:

1. Copiar os dados brutos do Postgres para a camada Bronze;
2. Preservar a informação original;
3. Depois executar transformações Bronze → Silver.

O ELT facilita a ingestão rápida e permite reaproveitar os dados brutos. Entretanto, sem organização e governança, o data lake pode se tornar um grande repositório de dados difíceis de localizar e interpretar.

## 7. Como os dados circulam entre sistemas

Existem três formas principais.

### Por meio de bancos de dados

Um processo escreve no banco e outro lê.

> **Exemplo:** o pipeline grava features em uma tabela e o serviço de predição consulta essa tabela.

É simples, mas pode ser lento e exige que os dois processos tenham acesso ao mesmo banco.

### Por meio de APIs

Um serviço envia uma requisição para outro e aguarda uma resposta.

Exemplo:

```http
POST /v1/agents/assessment/invoke
```

A API recebe os dados do formulário, chama o agente e devolve o resultado.

Esse modelo é chamado de *request-driven* e normalmente é **síncrono**. Se o serviço chamado estiver indisponível, a requisição pode falhar ou expirar.

REST é comum em APIs públicas. RPC costuma ser utilizado na comunicação interna entre serviços.

### Por meio de eventos e filas

Em arquiteturas maiores, os serviços podem se comunicar por meio de um *broker*, como Kafka ou RabbitMQ.

Exemplo:

1. O formulário publica o evento `assessment_submitted`;
2. Um *worker* consome a mensagem;
3. O agente executa a avaliação;
4. O resultado é armazenado;
5. Outro evento informa que o processamento terminou.

Essa arquitetura é **assíncrona** e reduz o acoplamento entre serviços. O produtor da mensagem não precisa esperar o consumidor terminar.

No modelo **pub/sub**, vários consumidores podem receber o mesmo evento. Em uma **message queue**, a mensagem normalmente é direcionada a um consumidor responsável pelo trabalho.

## 8. Processamento batch e streaming

### Batch

Processa dados acumulados em intervalos definidos.

Exemplos:

- executar diariamente o cálculo do tempo médio de resolução;
- atualizar toda noite as features de treinamento;
- gerar semanalmente indicadores de atendimento.

É adequado para informações que não precisam ser atualizadas imediatamente.

### Streaming

Processa os dados à medida que chegam ou em intervalos muito curtos.

Exemplos:

- detectar uma transação suspeita no momento em que ocorre;
- atualizar a quantidade de solicitações recebidas no último minuto;
- identificar imediatamente uma tentativa de *prompt injection*;
- processar eventos de uma fila de agentes.

Em ML, o batch costuma produzir **features estáticas**, como a média histórica de atendimentos. O streaming produz **features dinâmicas**, como o número de solicitações recebidas nos últimos cinco minutos.

Muitos sistemas precisam combinar os dois tipos.

> **Exemplo:** um sistema de priorização pode utilizar:
>
> - histórico de necessidades da família — *feature* batch;
> - disponibilidade atual de recursos — *feature* de streaming.

## Síntese final

A Engenharia de Dados sustenta o ciclo de vida dos sistemas de ML. As principais decisões envolvem:

- identificar e validar as fontes;
- escolher formatos adequados ao padrão de uso;
- definir modelos de dados coerentes com o problema;
- separar necessidades transacionais e analíticas;
- organizar processos ETL ou ELT;
- escolher entre banco, API ou eventos para transportar os dados;
- decidir quando usar batch, streaming ou uma combinação dos dois.

> O ponto mais importante é que **não existe uma única tecnologia ideal para todos os casos**. A arquitetura deve ser escolhida de acordo com o volume, a velocidade, o tipo dos dados, a latência esperada, as relações entre as entidades e a forma como as informações serão consumidas.
