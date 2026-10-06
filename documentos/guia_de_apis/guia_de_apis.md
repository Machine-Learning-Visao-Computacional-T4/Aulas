# Guia de APIs

## Sumário

- [1. O que é uma API](#1-o-que-é-uma-api)
- [2. Tipos de API](#2-tipos-de-api)
- [3. Fundamentos de APIs REST](#3-fundamentos-de-apis-rest)
  - [3.1 Princípios REST](#31-princípios-rest)
  - [3.2 Verbos HTTP](#32-verbos-http)
  - [3.3 Principais códigos de status HTTP](#33-principais-códigos-de-status-http)
- [4. Autenticação e Segurança](#4-autenticação-e-segurança)
- [5. Boas práticas de design de API](#5-boas-práticas-de-design-de-api)
- [6. Perguntas frequentes em entrevistas](#6-perguntas-frequentes-em-entrevistas)
- [7. Exemplo prático de requisição REST](#7-exemplo-prático-de-requisição-rest)
  - [7.1 Requisição (GET)](#71-requisição-get)
  - [7.2 Resposta com sucesso](#72-resposta-com-sucesso)
  - [7.3 Criando um recurso (POST)](#73-criando-um-recurso-post)
  - [7.4 Resposta da criação](#74-resposta-da-criação)
  - [7.5 Exemplo de erro (404)](#75-exemplo-de-erro-404)
- [8. Exemplos de código para consumir uma API](#8-exemplos-de-código-para-consumir-uma-api)
  - [8.1 Python — requests](#81-python--requests)
  - [8.2 Boas práticas ao consumir uma API](#82-boas-práticas-ao-consumir-uma-api)
- [9. Exercícios práticos (Python) — API DummyJSON](#9-exercícios-práticos-python--api-dummyjson)
  - [Exercício 1 — Primeira requisição](#exercício-1--primeira-requisição)
  - [Exercício 1.1 — Salvando os dados em pastas](#exercício-11--salvando-os-dados-em-pastas)
  - [Exercício 2 — Listando campos específicos](#exercício-2--listando-campos-específicos)
  - [Exercício 3 — Buscando um recurso específico por ID](#exercício-3--buscando-um-recurso-específico-por-id)
  - [Exercício 4 — Trabalhando com usuários](#exercício-4--trabalhando-com-usuários)
  - [Exercício 5 — Carrinhos](#exercício-5--carrinhos)
  - [Desafio extra — Um arquivo por item](#desafio-extra--um-arquivo-por-item)
  - [Bônus — Produto caro ou barato](#bônus--produto-caro-ou-barato)

**Conceitos essenciais e preparação para entrevistas técnicas**

## 1. O que é uma API

API significa **Application Programming Interface** (Interface de Programação de Aplicações). É um conjunto de regras e definições que permite que dois sistemas de software se comuniquem entre si, trocando dados e funcionalidades sem que um precise conhecer os detalhes internos de implementação do outro.

Na prática, uma API funciona como um "contrato": ela define quais requisições podem ser feitas, quais dados devem ser enviados e qual será o formato da resposta. Isso permite que aplicativos, sites, dispositivos e serviços diferentes conversem entre si de forma padronizada.

> **Analogia clássica:** pense em uma API como o cardápio de um restaurante. O cliente (aplicação que consome) não precisa saber como o prato é preparado na cozinha (o sistema interno). Ele apenas escolhe uma opção do cardápio (chama um *endpoint*) e recebe o prato pronto (a resposta).

## 2. Tipos de API

| Tipo | Características principais |
| --- | --- |
| **REST** | Baseada em HTTP, usa verbos (GET, POST, PUT, DELETE), recursos identificados por URLs, respostas geralmente em JSON. É o padrão mais usado hoje. |
| **SOAP** | Protocolo mais rígido e formal, usa XML, possui um padrão de contrato (WSDL). Comum em sistemas legados, bancos e governo. |
| **GraphQL** | Linguagem de consulta criada pelo Facebook. O cliente define exatamente quais campos quer receber, evitando *over-fetching* e *under-fetching*. |
| **gRPC** | Criado pelo Google, usa Protocol Buffers (binário) e HTTP/2. Muito rápido, comum em comunicação entre microsserviços. |
| **WebSocket** | Permite comunicação bidirecional e em tempo real entre cliente e servidor (ex.: chats, notificações ao vivo). |

## 3. Fundamentos de APIs REST

### 3.1 Princípios REST

- **Cliente-servidor:** separação clara entre quem consome e quem fornece os dados.
- **Stateless (sem estado):** cada requisição deve conter todas as informações necessárias; o servidor não guarda contexto entre chamadas.
- **Cacheável:** respostas podem indicar se podem ser armazenadas em cache para melhorar a performance.
- **Interface uniforme:** uso padronizado de URLs, verbos HTTP e formatos de dados.
- **Sistema em camadas:** o cliente não precisa saber se está falando diretamente com o servidor final ou com um intermediário (proxy, gateway, load balancer).

### 3.2 Verbos HTTP

| Verbo | Uso | Idempotente? |
| --- | --- | --- |
| `GET` | Buscar/ler um recurso | Sim |
| `POST` | Criar um novo recurso | Não |
| `PUT` | Atualizar/substituir um recurso por completo | Sim |
| `PATCH` | Atualizar parcialmente um recurso | Não (em geral) |
| `DELETE` | Remover um recurso | Sim |

> **Idempotente** significa que repetir a mesma requisição várias vezes produz o mesmo resultado final, sem efeitos colaterais adicionais.

### 3.3 Principais códigos de status HTTP

| Código | Categoria | Significado comum |
| --- | --- | --- |
| `200` | Sucesso | **OK** — requisição bem-sucedida |
| `201` | Sucesso | **Created** — recurso criado com sucesso |
| `204` | Sucesso | **No Content** — sucesso, sem corpo de resposta |
| `400` | Erro do cliente | **Bad Request** — requisição inválida |
| `401` | Erro do cliente | **Unauthorized** — falta autenticação |
| `403` | Erro do cliente | **Forbidden** — sem permissão |
| `404` | Erro do cliente | **Not Found** — recurso não encontrado |
| `409` | Erro do cliente | **Conflict** — conflito de estado (ex.: duplicidade) |
| `429` | Erro do cliente | **Too Many Requests** — limite de requisições excedido |
| `500` | Erro do servidor | **Internal Server Error** — erro genérico no servidor |
| `503` | Erro do servidor | **Service Unavailable** — servidor indisponível |

## 4. Autenticação e Segurança

- **API Key:** uma chave única enviada no header ou na URL para identificar o cliente.
- **Basic Auth:** usuário e senha codificados em Base64 enviados no header `Authorization`.
- **OAuth 2.0:** protocolo de autorização que permite acesso delegado sem compartilhar senha (usado por Google, Facebook, etc.).
- **JWT (JSON Web Token):** token assinado digitalmente que carrega informações do usuário e permite validação sem consultar o banco a cada requisição.
- **HTTPS:** essencial para criptografar os dados em trânsito e evitar interceptação.
- **CORS (Cross-Origin Resource Sharing):** mecanismo que controla quais origens (domínios) podem acessar a API a partir do navegador.

## 5. Boas práticas de design de API

- **Versionamento:** incluir a versão na URL (ex.: `/v1/usuarios`) ou no header, para evitar quebrar clientes existentes.
- **Nomes de recursos** no plural e em substantivos: `/usuarios`, não `/getUsuarios`.
- **Paginação:** retornar grandes listas em páginas (`limit`/`offset` ou cursores) para evitar sobrecarga.
- **Rate limiting:** limitar o número de requisições por cliente para proteger o serviço.
- **Mensagens de erro** claras e padronizadas, com código, mensagem e, se possível, um identificador de rastreamento.
- **Documentação:** usar padrões como OpenAPI/Swagger para descrever endpoints, parâmetros e respostas.

## 6. Perguntas frequentes em entrevistas

**P: O que é uma API e por que ela é importante?**

R: É uma interface que permite a comunicação entre sistemas diferentes, expondo funcionalidades e dados de forma padronizada, sem revelar a implementação interna. Ela é importante porque permite integração entre sistemas, reuso de funcionalidades e desacoplamento entre times/serviços.

**P: Qual a diferença entre PUT e PATCH?**

R: `PUT` substitui o recurso inteiro pelos dados enviados (se um campo não for enviado, ele pode ser apagado). `PATCH` atualiza apenas os campos enviados, mantendo o restante do recurso inalterado.

**P: O que significa uma API ser stateless?**

R: Significa que o servidor não guarda nenhum estado da sessão do cliente entre requisições. Cada requisição deve conter todas as informações necessárias (como o token de autenticação) para ser processada de forma independente.

**P: O que é idempotência e quais verbos HTTP são idempotentes?**

R: Idempotência é a propriedade de uma operação poder ser repetida várias vezes com o mesmo resultado final. `GET`, `PUT` e `DELETE` são idempotentes; `POST` geralmente não é, pois cada chamada pode criar um novo recurso.

**P: Qual a diferença entre autenticação e autorização?**

R: Autenticação verifica *quem* é o usuário (ex.: login com senha). Autorização define *o que* esse usuário autenticado tem permissão para fazer (ex.: acessar determinado recurso ou executar determinada ação).

**P: O que é rate limiting e por que ele é usado?**

R: É uma técnica para limitar o número de requisições que um cliente pode fazer em um período de tempo. É usado para proteger a API contra abuso, ataques de negação de serviço e para garantir uso justo entre os consumidores.

## 7. Exemplo prático de requisição REST

**Cenário:** buscar os dados de um usuário pelo ID.

### 7.1 Requisição (GET)

```http
GET /v1/usuarios/42 HTTP/1.1
Host: api.exemplo.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6...
Accept: application/json
```

### 7.2 Resposta com sucesso

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 42,
  "nome": "Ana Silva",
  "email": "ana.silva@exemplo.com",
  "criadoEm": "2026-03-10T14:32:00Z"
}
```

### 7.3 Criando um recurso (POST)

```http
POST /v1/usuarios HTTP/1.1
Host: api.exemplo.com
Content-Type: application/json

{
  "nome": "Carlos Souza",
  "email": "carlos@exemplo.com"
}
```

### 7.4 Resposta da criação

```http
HTTP/1.1 201 Created
Content-Type: application/json
Location: /v1/usuarios/43

{
  "id": 43,
  "nome": "Carlos Souza",
  "email": "carlos@exemplo.com",
  "criadoEm": "2026-09-15T10:05:00Z"
}
```

### 7.5 Exemplo de erro (404)

```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{
  "erro": "Usuário não encontrado",
  "codigo": "USER_NOT_FOUND"
}
```

> **Pontos-chave:** a URL identifica o recurso (`/usuarios/42`), o verbo HTTP indica a ação, e o código de status comunica o resultado antes mesmo de ler o corpo da resposta.

## 8. Exemplos de código para consumir uma API

Abaixo, exemplos de como buscar dados de uma API REST em Python.

### 8.1 Python — `requests`

```python
import requests

url = 'https://api.exemplo.com/v1/usuarios/42'
headers = {'Authorization': 'Bearer SEU_TOKEN'}

resposta = requests.get(url, headers=headers)
resposta.raise_for_status()  # lança erro se status >= 400
dados = resposta.json()
print(dados)

# POST
novo_usuario = {'nome': 'Carlos Souza', 'email': 'carlos@exemplo.com'}
resposta = requests.post(
    'https://api.exemplo.com/v1/usuarios',
    json=novo_usuario
)
print(resposta.status_code, resposta.json())
```

> Os endereços de `api.exemplo.com` são fictícios: este código serve de modelo e não roda como está.

### 8.2 Boas práticas ao consumir uma API

- Sempre verifique o código de status antes de usar os dados da resposta.
- Trate erros de rede (timeout, sem conexão) separadamente de erros da API (4xx/5xx).
- Nunca deixe tokens/senhas fixos no código: use variáveis de ambiente.
- Respeite limites de requisição (*rate limit*) informados pela API, geralmente nos headers de resposta.
- Use bibliotecas com suporte a *retry/backoff* para lidar com falhas temporárias.

## 9. Exercícios práticos (Python) — API DummyJSON

Exercícios para praticar consumo de API usando Python e a biblioteca `requests`, com dados reais de uma API pública e gratuita:

- Produtos: <https://dummyjson.com/products>
- Usuários: <https://dummyjson.com/users>
- Carrinhos: <https://dummyjson.com/carts>

**Setup** — rode antes de tudo:

```python
import requests
```

### Exercício 1 — Primeira requisição

Faça uma requisição `GET` para `https://dummyjson.com/products`, imprima o código de status da resposta e o total de produtos (campo `"total"` do JSON).

#### Resolução

```python
url = "https://dummyjson.com/products"

resposta = requests.get(url)
print("Status:", resposta.status_code)

dados = resposta.json()
print("Total de produtos:", dados["total"])
```

### Exercício 1.1 — Salvando os dados em pastas

**Objetivo:** criar pastas e salvar os dados da API em arquivos `.json`, cada tipo de dado na sua própria pasta (`produtos/`, `usuarios/`, `carrinhos/`).

**Novos conceitos:**

- `import os` para trabalhar com pastas;
- `os.makedirs("pasta", exist_ok=True)` cria uma pasta sem dar erro se ela já existir;
- `import json` e `json.dump(dados, arquivo)` escrevem um dicionário/lista Python como JSON dentro de um arquivo aberto.

#### Resolução

```python
import os
import json

# Criar as pastas
os.makedirs("produtos", exist_ok=True)
os.makedirs("usuarios", exist_ok=True)
os.makedirs("carrinhos", exist_ok=True)

# --- Produtos ---
resposta = requests.get("https://dummyjson.com/products")
dados_produtos = resposta.json()
with open("produtos/produtos.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_produtos, arquivo, ensure_ascii=False, indent=2)

# --- Usuários ---
resposta = requests.get("https://dummyjson.com/users")
dados_usuarios = resposta.json()
with open("usuarios/usuarios.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_usuarios, arquivo, ensure_ascii=False, indent=2)

# --- Carrinhos ---
resposta = requests.get("https://dummyjson.com/carts")
dados_carrinhos = resposta.json()
with open("carrinhos/carrinhos.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_carrinhos, arquivo, ensure_ascii=False, indent=2)

print("Arquivos salvos!")
for pasta in ["produtos", "usuarios", "carrinhos"]:
    print(f"{pasta}/:", os.listdir(pasta))
```

Resultado esperado (estrutura de pastas):

```text
produtos/
    produtos.json
usuarios/
    usuarios.json
carrinhos/
    carrinhos.json
```

### Exercício 2 — Listando campos específicos

Percorra a lista de produtos (campo `"products"`) e imprima o título e o preço de cada um.

#### Resolução

```python
url = "https://dummyjson.com/products"
resposta = requests.get(url)
dados = resposta.json()

for produto in dados["products"]:
    print(f'{produto["title"]} - ${produto["price"]}')
```

### Exercício 3 — Buscando um recurso específico por ID

Busque o produto de ID 5 em `https://dummyjson.com/products/5` e imprima nome, categoria e estoque.

#### Resolução

```python
produto_id = 5
url = f"https://dummyjson.com/products/{produto_id}"

resposta = requests.get(url)
produto = resposta.json()

print("Nome:", produto["title"])
print("Categoria:", produto["category"])
print("Estoque:", produto["stock"])
```

### Exercício 4 — Trabalhando com usuários

Busque o usuário de ID 10 em `https://dummyjson.com/users/10`, junte `firstName` e `lastName`, e imprima o nome completo e o email.

#### Resolução

```python
url = "https://dummyjson.com/users/10"
resposta = requests.get(url)
usuario = resposta.json()

nome_completo = f'{usuario["firstName"]} {usuario["lastName"]}'
print("Nome completo:", nome_completo)
print("Email:", usuario["email"])
```

### Exercício 5 — Carrinhos

Busque o carrinho de ID 1 em `https://dummyjson.com/carts/1` e imprima quantos produtos diferentes ele tem (`len` da lista `"products"`) e o valor total (`"total"`).

#### Resolução

```python
url = "https://dummyjson.com/carts/1"
resposta = requests.get(url)
carrinho = resposta.json()

qtd_produtos = len(carrinho["products"])
print("Quantidade de produtos diferentes:", qtd_produtos)
print("Valor total:", carrinho["total"])
```

### Desafio extra — Um arquivo por item

Em vez de salvar um arquivo só com a lista inteira, salve um arquivo para cada item dentro da pasta (ex.: `produto_1.json`, `produto_2.json`...).

#### Resolução

```python
import os
import json

os.makedirs("produtos", exist_ok=True)

resposta = requests.get("https://dummyjson.com/products")
dados_produtos = resposta.json()

for produto in dados_produtos["products"]:
    nome_arquivo = f"produtos/produto_{produto['id']}.json"
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(produto, arquivo, ensure_ascii=False, indent=2)

print("Um arquivo por produto salvo em produtos/")
```

### Bônus — Produto caro ou barato

Busque o produto de ID 1. Se o preço for maior que 10, imprima `"Produto caro"`; caso contrário, `"Produto barato"`.

#### Resolução

```python
produto_id = 1
url = f"https://dummyjson.com/products/{produto_id}"

resposta = requests.get(url)
produto = resposta.json()

if produto["price"] > 10:
    print("Produto caro")
else:
    print("Produto barato")
```
