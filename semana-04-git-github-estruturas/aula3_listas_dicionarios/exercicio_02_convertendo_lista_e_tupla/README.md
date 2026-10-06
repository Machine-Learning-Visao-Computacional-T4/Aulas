# Exercício 02 — Mãos à obra + commit: convertendo entre lista e tupla

**Tipo:** prática + commit · 12 min

## Objetivo
Praticar **tuplas** e a conversão entre os dois tipos, reforçando o fluxo de versionamento.

## O que fazer
1. Crie um arquivo `tuplas.py` com uma **tupla** representando os 3 dias da semana que você mais gosta.
2. Converta essa tupla em lista usando `list()`, adicione um novo dia, e converta de volta para tupla usando `tuple()`.
3. Imprima o resultado em **cada etapa**.
4. Commit (mensagem descritiva) e push para o GitHub.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_listas_dicionarios/exercicio_02_convertendo_lista_e_tupla/tuplas.py
```

No Windows, se `python` não funcionar, use `py aula3_listas_dicionarios/exercicio_02_convertendo_lista_e_tupla/tuplas.py`.

## Exemplo de execução

```text
Tupla original: ('sexta', 'sábado', 'domingo')
Como lista, com um dia novo: ['sexta', 'sábado', 'domingo', 'quinta']
De volta a tupla: ('sexta', 'sábado', 'domingo', 'quinta')
Tipo final: <class 'tuple'>
```

## Dicas e erros comuns
- A tupla é **imutável**, mas dá para "contornar" convertendo para lista, alterando e convertendo de volta. Na verdade, você cria uma tupla nova.
- Use tupla quando os dados não devem mudar (coordenadas, dias da semana fixos).
