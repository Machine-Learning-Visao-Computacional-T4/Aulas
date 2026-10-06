# Exercício 05 — Conectando o Google Colab ao GitHub

**Tipo:** prática · alternativa completa para quem não instala Python/VS Code

> Se o seu computador é mais antigo, tem pouco espaço em disco, ou você simplesmente prefere não instalar nada, **dá para seguir todo o curso, incluindo o versionamento, 100% pelo Colab.** Não é um "plano B" inferior.

## Parte A — Abrir um repositório do GitHub dentro do Colab
1. No Google Colab, vá em **File → Open notebook**.
2. Clique na aba **GitHub** e autorize o Colab a acessar sua conta, se pedido.
3. Digite o nome do seu repositório na busca e selecione-o.
4. Para salvar de volta: **File → Save a copy in GitHub**, escolhendo o mesmo repositório.

Essa é a forma mais simples, sem comandos de terminal.

## Parte B — Commit e push de dentro de uma célula
Também é possível usar comandos Git em uma célula, com `!` na frente:

```python
!git add .
!git commit -m "Exercício da aula concluído"
!git push
```

Antes de o `push` funcionar, é preciso **autenticar**, porque o Colab não faz login visual como o GitHub Desktop. O caminho é usar um **Personal Access Token** (token de acesso pessoal) do GitHub. O professor demonstra esse passo ao vivo.

### Cuidados com o token
- Um token é como uma **senha**: nunca o escreva dentro de um notebook ou arquivo que será enviado ao GitHub, nem o compartilhe.
- Dê ao token só a permissão necessária e um prazo de validade curto.
- Se vazar, **apague o token** nas configurações do GitHub e crie outro.

> Este guia da Parte B resume o caminho; siga a demonstração feita em aula para os detalhes da autenticação, pois a interface do GitHub e do Colab muda com frequência.
