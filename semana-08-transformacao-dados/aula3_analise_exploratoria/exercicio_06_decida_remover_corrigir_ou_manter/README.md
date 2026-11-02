# Exercício 06 — Decida: remover, corrigir ou manter?

**Tipo:** dinâmica + script · 8 min

## Objetivo
Praticar a decisão sobre cada problema encontrado, justificando.

## O que fazer
1. Veja a lista de problemas: duplicados, `qtd` -1, `qtd` 40, tempo 480, canal em 9 variações, cliente ausente no balcão.
2. Em duplas, escolham para cada problema **remover**, **corrigir** ou **manter**, e escrevam a justificativa.
3. Rode o script, que aplica **uma** possível resposta, e compare as decisões com as da turma.
4. Conclusão: toda decisão deve ser **registrada** e, se possível, validada com quem conhece o negócio.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_analise_exploratoria/exercicio_06_decida_remover_corrigir_ou_manter/decisoes.py
```

No Windows, se `python` não funcionar, use `py aula3_analise_exploratoria/exercicio_06_decida_remover_corrigir_ou_manter/decisoes.py`.

**No Google Colab:** abra [colab.research.google.com](https://colab.research.google.com), crie um notebook novo, cole o conteúdo do arquivo `decisoes.py` em uma célula e execute com `Shift + Enter`. Antes, envie para o Colab os **arquivos de dados desta pasta** (`pedidos.csv`, `produtos.csv`); veja o [guia](../../docs/guia_eda.md#no-google-colab). Instale o que faltar com `!pip install pandas numpy matplotlib seaborn`.

## Exemplo de execução

```text
                       linhas  faturamento  tempo_max
bruto                     687      11085.5      480.0
limpo                     675      10985.5       58.0
limpo e só qtd válida     668       9383.5       58.0

Faturamento por mês:
      bruto  qtd válida
mes
1    1536.0      1522.0
2    1876.0      1501.0
3    2638.0      1652.0
4    1411.0      1380.0
5    1904.0      1896.0
6    1721.0      1432.0

Canais depois: ['App', 'Balcão', 'Delivery']
```

## Dicas e erros comuns
- | Problema | Decisão sugerida |
| --- | --- |
| Linhas duplicadas | Remover com `drop_duplicates()` |
| Quantidade inválida (-1 ou 40) | Investigar com o negócio; excluir da análise de faturamento |
| Tempo de entrega de 480 min | Tratar como nulo se for código de erro |
| Pedido sem cliente (balcão) | Manter: são vendas de balcão não identificadas |
| Pedido sem avaliação | Manter; não imputar a nota |
| Canal com 9 grafias | Corrigir com `.str.strip().str.title()` |
- O pico de março desaparece quando os pedidos de 40 unidades saem da conta: era um problema de dados, não de negócio.
