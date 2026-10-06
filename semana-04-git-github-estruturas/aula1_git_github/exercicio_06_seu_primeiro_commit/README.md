# Exercício 06 — Seu primeiro commit

**Tipo:** prática · o momento mais importante da aula

## Objetivo
Fazer, do início ao fim, o **ciclo completo**: **editar → commitar → enviar** uma mudança para o GitHub.

## Passo a passo (GitHub Desktop)
1. No GitHub Desktop, clone o repositório `meu-primeiro-repositorio` criado antes: **File → Clone Repository**.
2. Abra o arquivo `README.md` em qualquer editor de texto e **adicione uma frase sobre você**. Salve.
3. Volte ao GitHub Desktop: suas mudanças aparecem na aba **Changes**.
4. Escreva uma **mensagem de commit** (por exemplo, `Adiciona apresentação pessoal`), clique em **Commit to main** e depois em **Push origin**.
5. Atualize a página do repositório no navegador: a sua frase já está lá.

## O mesmo pelo terminal
```bash
git clone https://github.com/SEU_USUARIO/meu-primeiro-repositorio.git
cd meu-primeiro-repositorio

# (edite o README.md e salve)

git status                      # mostra o que mudou
git add README.md               # escolhe o que vai no commit
git commit -m "Adiciona apresentação pessoal"
git push                        # envia para o GitHub
```

## Boas mensagens de commit
Uma boa mensagem **explica o que mudou**. Prefira `Adiciona apresentação pessoal` a `mudanças` ou `ajustes`.

## Problemas comuns
- **`git push` pede login:** entre com a mesma conta do GitHub (o navegador abre para autenticar).
- **Não aparece nada em Changes:** você salvou o arquivo? Está na pasta clonada?
