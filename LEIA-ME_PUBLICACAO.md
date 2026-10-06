# Como publicar estes repositórios

Esta pasta contém **5 repositórios prontos**, cada um em sua subpasta:

| Pasta | Vira o repositório | Observação |
| --- | --- | --- |
| `.github/` | `Machine-Learning-Visao-Computacional-T4/.github` | O arquivo `profile/README.md` aparece como **capa da organização**. Precisa ser **público**. |
| `semana-02-pipeline-ml/` | `Machine-Learning-Visao-Computacional-T4/semana-02-pipeline-ml` | |
| `semana-03-logica-python/` | `Machine-Learning-Visao-Computacional-T4/semana-03-logica-python` | |
| `semana-04-git-github-estruturas/` | `Machine-Learning-Visao-Computacional-T4/semana-04-git-github-estruturas` | |
| `semana-05-arquivos-datas-funcoes/` | `Machine-Learning-Visao-Computacional-T4/semana-05-arquivos-datas-funcoes` | |

## Opção A — script (mais rápido)
1. Instale o [GitHub CLI](https://cli.github.com) e faça login: `gh auth login`.
2. Na pasta que contém este arquivo, rode: `bash publicar_repositorios.sh`.

O script cria cada repositório na organização, faz o primeiro commit e o push.

## Opção B — manual, pelo site
Para cada pasta:
1. No GitHub, **New repository** dentro da organização `Machine-Learning-Visao-Computacional-T4` (nome igual ao da pasta, **Public**, **sem** README/.gitignore/licença, que já existem).
2. No terminal, dentro da pasta:
   ```bash
   git init -b main
   git add .
   git commit -m "Versão inicial do material"
   git remote add origin https://github.com/Machine-Learning-Visao-Computacional-T4/NOME-DO-REPOSITORIO.git
   git push -u origin main
   ```

## Depois de publicar
- Abra [github.com/Machine-Learning-Visao-Computacional-T4](https://github.com/Machine-Learning-Visao-Computacional-T4) e confira se a capa aparece.
- Para os alunos poderem fazer **fork**, os repositórios precisam ser públicos (ou a organização deve permitir forks de repositórios privados).
- Se quiser que o README mostre os repositórios em destaque, fixe-os (*Customize pins*) na página da organização.
