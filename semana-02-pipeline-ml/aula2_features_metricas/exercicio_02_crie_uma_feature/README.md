# Exercício 02 — Crie uma feature

**Tipo:** brainstorm + script

## Objetivo
Praticar a criação de **features derivadas** a partir de variáveis brutas de um cenário realista.

## Cenário
Um app de entrega tem estas variáveis brutas por pedido: **hora do pedido, distância, valor do pedido e número de pedidos anteriores do cliente**.

Exemplos de features derivadas: *"pedido em horário de pico?"*, *"valor médio por pedido do cliente"*.

## Passo a passo
1. **Antes de rodar o script**, escreva pelo menos **2 features** que você criaria e **por que cada uma ajudaria o modelo**.
2. Rode o script de exemplo:
   ```bash
   pip install -r requirements.txt   # uma vez, na raiz do repositório
   python aula2_features_metricas/exercicio_02_crie_uma_feature/features_entrega.py
   ```
3. Veja a tabela original e a tabela com as features novas.
4. Abra `features_entrega.py`, **adicione a sua própria feature** no bloco marcado `# SUA FEATURE AQUI` e rode de novo.
5. Compartilhe 1 feature com a turma e explique por que ela ajudaria.

## Para pensar
- A feature usa só informação que **existiria na hora de prever**? (Cuidado com vazamento de dados.)
- Um especialista do domínio (um entregador, um gerente de restaurante) sugeriria alguma feature que você não pensou?
