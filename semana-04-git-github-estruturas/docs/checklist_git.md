# Checklist Git para todo exercício

Leve para o resto do curso (e para projetos pessoais e profissionais).

| Passo | Pergunta-chave |
| --- | --- |
| Escrever o código | O programa funciona e foi testado? |
| `git add` / stage | As mudanças certas foram selecionadas? |
| `git commit -m "..."` | A mensagem explica claramente o que mudou? |
| `git push` | As mudanças realmente aparecem no GitHub? |
| Branch (quando fizer sentido) | Essa mudança merece uma branch separada? |

## O fluxo em 4 passos
1. **Ambiente:** VS Code aberto com o repositório clonado (ou Colab conectado ao GitHub).
2. **Código:** um arquivo `.py` novo ou alterado.
3. **Teste:** rode e confira a saída no terminal.
4. **Versionamento:** `git add`, `git commit -m "mensagem clara"`, `git push` (ou os botões equivalentes).

## Boas práticas de organização
- **Uma pasta por projeto**; não misture exercícios completamente diferentes.
- **Nomes de arquivo descritivos:** `calculadora_imc.py` é melhor que `teste2.py`.
- **README atualizado** explicando o que cada pasta contém.
- **`requirements.txt`**: lista as bibliotecas externas do projeto (aparece quando o curso usar bibliotecas de ML).

## Em dúvida? `git status`
É o comando que mostra o que mudou e qual é o próximo passo.
