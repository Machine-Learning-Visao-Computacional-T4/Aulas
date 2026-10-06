# Exercício 06 — Mãos à obra + commit: seu próprio módulo

**Tipo:** prática + commit · 18 min

## Objetivo
Criar um **módulo próprio** e importá-lo em outro arquivo.

## O que fazer
1. Crie `texto.py` com 3 funções: `so_digitos(texto)`, `normalizar_nome(nome)` e `formatar_data(texto)` (converte `dd/mm/aaaa` para `AAAA-MM-DD`).
2. Adicione um bloco `if __name__ == "__main__":` com **3 testes simples**.
3. Crie `principal.py` que **importa `texto`** e usa as 3 funções com exemplos.
4. Commit e push dos **dois arquivos**.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_funcoes_modulos/exercicio_06_seu_proprio_modulo/principal.py
```

No Windows, se `python` não funcionar, use `py aula3_funcoes_modulos/exercicio_06_seu_proprio_modulo/principal.py`.

## Exemplo de execução

```text
48988885678
Bruno Lima
2025-03-18
```

## Dicas e erros comuns
- Os dois arquivos precisam estar **na mesma pasta**. Se aparecer `ModuleNotFoundError: No module named 'texto'`, é quase sempre isso.
- As funções são as mesmas da Aula 2: o ganho é **organização e reutilização**.
- Nome de módulo não pode ter espaço nem hífen: use `texto.py`, não `meu-texto.py`.

## Testando o módulo sozinho
O bloco `if __name__ == "__main__":` de `texto.py` roda **só** quando você executa o módulo diretamente:

```bash
python aula3_funcoes_modulos/exercicio_06_seu_proprio_modulo/texto.py
```
