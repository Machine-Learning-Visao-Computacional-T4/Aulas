#!/usr/bin/env bash
# Publica os repositórios da Turma T4 na organização do GitHub.
# Pré-requisitos: Git e GitHub CLI (gh) instalados, e "gh auth login" já feito
# com uma conta que possa CRIAR repositórios em Machine-Learning-Visao-Computacional-T4.
set -euo pipefail

ORG="Machine-Learning-Visao-Computacional-T4"
cd "$(dirname "$0")"

publicar() {
  repo="$1"; descricao="$2"
  echo "==> Publicando $ORG/$repo"
  ( cd "$repo"
    git init -q -b main
    git add .
    git commit -q -m "Versão inicial do material"
    gh repo create "$ORG/$repo" --public --description "$descricao" --source=. --remote=origin --push
  )
}

publicar ".github" "Página de apresentação da Turma T4 (README de capa)"
publicar "semana-02-pipeline-ml" "Semana 02: pipeline de ML, métricas, overfitting e produção"
publicar "semana-03-logica-python" "Semana 03: lógica de programação com Python"
publicar "semana-04-git-github-estruturas" "Semana 04: Git, GitHub, Python local e estruturas de dados"
publicar "semana-05-arquivos-datas-funcoes" "Semana 05: arquivos, datas, regex, funções e módulos"

echo "Pronto! Veja: https://github.com/$ORG"
