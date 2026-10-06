# Exercício 05 — Exercício final do módulo: sua agenda de contatos

**Tipo:** projeto de encerramento · 20 min

## Objetivo
Consolidar todo o módulo (**Git/GitHub, ambiente e estruturas de dados**) em um projeto completo, reativando o conceito de **branch**.

## O que fazer
1. Crie uma nova **branch** chamada `feature/agenda-contatos` no seu repositório.
2. Nessa branch, crie um arquivo `agenda.py` com **pelo menos 5 contatos** e uma **função para buscar um contato pelo nome**.
3. Teste seu programa, faça o **commit** e envie (**push**) a branch para o GitHub.
4. Se der tempo, abra um **Pull Request** da sua branch para a `main` e faça o **merge**.

## Como executar

**No VS Code (ou qualquer terminal)**, a partir da pasta raiz do repositório:

```bash
python aula3_listas_dicionarios/exercicio_05_agenda_de_contatos_projeto_final/agenda.py
```

No Windows, se `python` não funcionar, use `py aula3_listas_dicionarios/exercicio_05_agenda_de_contatos_projeto_final/agenda.py`.

## Exemplo de execução

```text
Nome para buscar: bruno
Encontrado: Bruno Lima | (48) 98888-2222 | São José
```

(Os valores digitados no exemplo acima foram: `bruno`.)

## Dicas e erros comuns
- `agenda.py` é uma **solução de exemplo**; a sua pode ter outros campos. Use **só dados fictícios**.
- Se der erro ao enviar a branch pela primeira vez, use exatamente `git push -u origin feature/agenda-contatos`.

## O fluxo de Git deste exercício, no terminal

```bash
git switch -c feature/agenda-contatos        # 1. cria a branch e vai para ela
# (crie e teste o agenda.py)
git add agenda.py
git commit -m "Adiciona agenda de contatos com busca por nome"
git push -u origin feature/agenda-contatos   # 2. envia a branch (a 1ª vez usa -u)
```

Depois, no GitHub: aparece um aviso **Compare & pull request**. Clique, descreva o que o programa faz, **Create pull request** e então **Merge pull request**. Para atualizar seu computador:

```bash
git switch main
git pull
```
