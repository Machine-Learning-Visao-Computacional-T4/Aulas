# Guia: Python, VS Code, Git e GitHub

Vamos criar um programa que lê uma tabela de notas e colocar o projeto no GitHub. O guia serve para **Windows** e **Mac**. Digite cada comando separadamente e pressione **Enter**.

| Ferramenta | O que faz |
| --- | --- |
| **Python** | Executa nosso programa. |
| **VS Code** | Abre a pasta e permite escrever os arquivos. |
| **Git** | Registra versões do projeto no computador. |
| **GitHub** | Guarda o repositório na internet. |

> **Terminal** é a janela para digitar comandos.

---

## Parte 1 — Preparar o computador

### 1. Verificar se já existe Python

No Windows, abra o menu Iniciar, procure **PowerShell** e abra-o. No Mac, procure o aplicativo **Terminal**. Digite somente o comando correspondente ao seu sistema:

**Windows**

```powershell
py --version
```

**Mac**

```bash
python3 --version
```

- Se aparecer `Python 3.x.x`, você já tem Python: vá para o **passo 3**. O número exato da versão pode variar.
- Se aparecer "comando não encontrado" ou "não é reconhecido", siga o **passo 2**.

### 2. Instalar Python (somente se necessário)

1. Acesse [python.org/downloads](https://www.python.org/downloads/).
2. Baixe a versão indicada para seu sistema, Windows ou macOS.
3. Abra o arquivo baixado e siga as instruções. No Windows, se aparecer **Add Python to PATH**, marque essa opção.
4. Feche e abra o PowerShell ou Terminal novamente. Repita o comando do passo 1. Só avance quando aparecer a versão do Python.

### 3. Instalar VS Code (se necessário)

> Caso você já tenha o VS Code, não precisa instalar: siga adiante.

Acesse [code.visualstudio.com/download](https://code.visualstudio.com/download).

- **Windows:** abra o instalador e siga as etapas.
- **Mac:** abra o arquivo `.dmg` e arraste **Visual Studio Code** para **Aplicativos**.

Depois, abra o programa.

### 4. Instalar a extensão Python

No VS Code, clique em **Extensions/Extensões** (ícone de blocos na barra lateral), procure **Python**, selecione a extensão publicada pela **Microsoft** e clique em **Install/Instalar**.

> A extensão ajuda o editor; ela **não** substitui o Python instalado no computador.

### 5. Verificar Git e a conta no GitHub

Abra um terminal e digite:

```bash
git --version
```

Se aparecer um número de versão, o Git está disponível. Se não, instale pelo [site oficial do Git](https://git-scm.com/downloads), reabra o terminal e teste novamente. No Mac, uma janela do sistema também pode oferecer a instalação das ferramentas necessárias; siga as instruções dela.

Crie uma conta em [github.com](https://github.com) se ainda não tiver uma.

> **Git e GitHub são coisas diferentes:** instalar o Git não cria a conta.

---

## Parte 2 — Escolha um caminho

Temos duas possibilidades. Na aula de hoje trabalharemos com o **Caminho A**. O Caminho B será mencionado e poderá ser testado posteriormente.

| Caminho | Descrição |
| --- | --- |
| **A** | Criar no GitHub e depois copiar o projeto para o computador. |
| **B** | Começar com uma pasta no computador e depois publicá-la no GitHub. |

Usaremos o nome `meu_primeiro_projeto`. Nos comandos, troque `SEU_USUARIO` pelo nome da sua conta no GitHub.

---

## Caminho A — Criar primeiro no GitHub

### A1. Criar o repositório

1. Acesse [github.com/new](https://github.com/new).
2. Em **Repository name**, escreva `meu_primeiro_projeto` (ou um nome da sua preferência; nesse caso, substitua-o onde for necessário).
3. Escolha **Public** ou **Private**.
4. Marque **Add a README file**.
5. Clique em **Create repository**.

Agora o GitHub já tem um README e um primeiro commit.

### A2. Copiar para o computador

Na página do repositório, clique em **Code → HTTPS** e copie a URL. Abra o PowerShell (Windows) ou Terminal (Mac) e vá para Documentos:

> A sugestão é usar a pasta Documentos. Se preferir outra, pode usar, desde que saiba onde estão sua pasta e seu projeto.

**Windows (PowerShell)**

```powershell
cd "$HOME\Documents"
```

**Mac**

```bash
cd ~/Documents
```

Se sua pasta Documentos estiver em outro local, navegue até a pasta onde deseja guardar o projeto. Depois execute, com sua URL real:

```bash
git clone https://github.com/SEU_USUARIO/meu_primeiro_projeto.git
cd meu_primeiro_projeto
git status
```

`git clone` cria a pasta `meu_primeiro_projeto` no computador e traz o histórico.

> **Atenção:** não crie manualmente uma pasta de mesmo nome antes. Não use `git init` nesse caminho, pois o clone já configurou o Git e a conexão com o GitHub.

### A3. Abrir o projeto
No VS Code, use File → Open Folder... para abrir a pasta criada pelo clone.

### A4. Criar uma branch para o seu trabalho

Antes de criar ou alterar qualquer arquivo, crie uma **branch**: uma linha de trabalho separada, que deixa a `main` intacta. No terminal, dentro da pasta do projeto:

```bash
git switch -c feat/meu-primeiro-projeto
git branch
```

- `git switch -c` cria a branch e já muda para ela;
- `feat/meu-primeiro-projeto` é o nome (curto, sem espaços e sem acentos);
- `git branch` lista as branches: o `*` deve estar em `feat/meu-primeiro-projeto`.

Outra opção, que faz exatamente a mesma coisa, é o comando `git checkout -b`:

```bash
git checkout -b feat/meu-primeiro-projeto
```

Use o que preferir. O `git switch` é mais novo e só troca de branch; o `git checkout` é mais antigo e faz outras coisas além disso, mas é muito comum em tutoriais e funciona em qualquer versão do Git.

> Se preferir o VS Code, clique no nome da branch no canto inferior esquerdo (geralmente `main`), escolha **Create new branch...**, digite o nome e pressione **Enter**.

Os detalhes sobre branches estão na [Parte 3](#parte-3--trabalhar-com-branches).

### A5. Criar o arquivo e testar o programa

No VS Code crie um arquivo `exercicio1.py` e teste

```
age = 18
if age >= 18:
    print('de maior')
else:
    print('de menor')
```

Salve tudo. Abra **Terminal → New Terminal** no VS Code e execute:

**Windows**

```powershell
py exercicio1.py
```

**Mac**

```bash
python3 exercicio1.py
```

Você deve ver:

```text
de maior
```

### A6. Registrar e enviar as mudanças

No terminal do projeto, execute um comando por vez:

```bash
git status
git add .
git status
git commit -m "Adiciona o primeiro arquivo"
git push -u origin feat/meu-primeiro-projeto
```

- O primeiro `git status` mostra o que mudou; o segundo mostra o que foi selecionado.
- O `commit` registra a versão no computador, dentro da sua branch; o `push` envia essa branch ao GitHub.
- O `-u` (usado só no primeiro envio da branch) liga a branch do computador à do GitHub. Nos próximos envios, basta `git push`.

Se o Git pedir nome e e-mail, configure-os e repita o commit (se não pedir, passse para frente):

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@example.com"
```

Substitua os exemplos pelo nome e e-mail que deseja associar aos commits.

Atualize a página do GitHub. Vai aparecer um aviso amarelo com o botão **Compare & pull request**. Seu arquivo está na sua branch; para juntá-lo à `main`, você abre um **Pull Request**, um pedido para incorporar as mudanças da sua branch. Veja [o que é um Pull Request](#o-que-é-um-pull-request) e siga os passos [C6 a C9 da Parte 3](#c6-abrir-o-pull-request).

Quando você voltar ao seu editor de código (por exemplo o VS code), volte para a main:
`git checkout main`

Traga os updates do seu projeto do GitHub para a sua máquina
`git pull`

> Terminou o Caminho A. **Não** faça o Caminho B com essa mesma pasta, caso você queira fazer o caminho B, use um outro nome de projeto.

---

## Resumo para lembrar

| Ação | Resultado |
| --- | --- |
| Salvar com `Ctrl+S` ou `⌘S` | Grava o arquivo no computador. |
| `git add .` | Seleciona mudanças para o próximo commit. |
| `git commit -m "mensagem"` | Registra uma versão no Git local. |
| `git push` | Envia commits ao GitHub. |
| `git pull` | Traz para o computador mudanças feitas no GitHub. |
| `git status` | Mostra o estado atual do projeto. |
| `git branch` | Lista as branches e mostra em qual você está. |
| `git switch -c nome` ou `git checkout -b nome` | Cria uma branch nova e muda para ela. |
| `git switch nome` ou `git checkout nome` | Muda para uma branch existente. |
| `git push -u origin nome` | Envia uma branch nova ao GitHub (primeira vez). |
| Pull Request (no GitHub) | Pede para juntar as mudanças da sua branch na `main`, com revisão. |
| `git switch main` e `git pull` | Volta para a `main` e traz para o computador o que foi aprovado e juntado. |

> ⚠️ **Nunca** coloque senhas, chaves de API ou dados pessoais no repositório. Um repositório público pode ser visto por outras pessoas.

---

## Caminho B — Criar primeiro no computador

### B1. Criar e abrir a pasta

1. No Explorador de Arquivos (Windows) ou Finder (Mac), abra Documentos e crie a pasta `meu_primeiro_projeto`. Lembre-se de onde a salvou.
2. No VS Code, use **File → Open Folder...** (Arquivo → Abrir Pasta...) e selecione a pasta inteira.
3. Na barra lateral, passe o mouse pelo nome da pasta e clique em **New File/Novo Arquivo**. Crie estes três arquivos, um de cada vez:

| Arquivo | Para que serve |
| --- | --- |
| `README.md` | Explica o projeto. |
| `dados.csv` | Guarda a tabela de notas. |
| `analisar.py` | Contém o programa Python. |

Em `README.md`, escreva:

```markdown
# Meu primeiro projeto

Este projeto lê um arquivo CSV e mostra o nome e a nota de cada aluno.
```

Em `dados.csv`, escreva:

```csv
nome,nota
Ana,8
Bruno,7
Carla,9
```

A primeira linha traz os nomes das colunas. As outras são os dados.

Em `analisar.py`, escreva (com os espaços no início das linhas):

```python
import csv

with open("dados.csv", encoding="utf-8") as arquivo:
    dados = csv.DictReader(arquivo)
    for aluno in dados:
        print(aluno["nome"], aluno["nota"])
```

O programa abre o CSV, passa por cada aluno e mostra o nome e a nota. Salve os arquivos com `Ctrl+S` (Windows) ou `⌘S` (Mac).

### B2. Testar o programa

No VS Code, clique em **Terminal → New Terminal**. O terminal deve estar dentro de `meu_primeiro_projeto`. Digite `pwd`: o caminho mostrado deve terminar com o nome dessa pasta. Se estiver em outra pasta, abra a pasta certa no VS Code e crie um terminal novo.

Execute:

**Windows**

```powershell
py analisar.py
```

**Mac**

```bash
python3 analisar.py
```

Resultado esperado:

```text
Ana 8
Bruno 7
Carla 9
```

> Se aparecer `FileNotFoundError`, confira se o terminal está na pasta correta e se o arquivo realmente se chama `dados.csv`.

### B3. Iniciar o Git e registrar a primeira versão

No terminal da pasta do projeto, execute um comando por vez:

```bash
git init
git branch -M main
git status
git add .
git status
git commit -m "Cria projeto de analise de notas"
```

- `git init` inicia o histórico no computador.
- `main` é o nome da branch principal.
- `git status` mostra o estado dos arquivos; antes do `git add`, eles aparecem como *untracked*.
- O ponto em `git add .` seleciona os arquivos da pasta.
- `git commit` registra uma versão, mas ainda **não** envia nada à internet.

Se o Git pedir nome e e-mail, configure-os e repita o commit:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@example.com"
```

Substitua os exemplos pelo nome e e-mail que deseja associar aos commits.

### B4. Criar o repositório no GitHub

1. Acesse [github.com/new](https://github.com/new).
2. Em **Repository name**, escreva `meu_primeiro_projeto`.
3. Escolha **Public** ou **Private**, conforme a orientação da aula.
4. **Não** marque as opções para adicionar README, `.gitignore` ou licença: o projeto já tem arquivos e commit no computador.
5. Clique em **Create repository** e copie a URL HTTPS mostrada na página.

Ela terá a forma `https://github.com/SEU_USUARIO/meu_primeiro_projeto.git`. Copie a URL pura, sem colchetes ou parênteses de Markdown.

### B5. Conectar e enviar

Volte ao terminal do projeto. No primeiro comando, substitua `SEU_USUARIO` pelo seu usuário real:

```bash
git remote add origin https://github.com/SEU_USUARIO/meu_primeiro_projeto.git
git remote -v
git push -u origin main
```

- `origin` é um apelido para o endereço no GitHub.
- `git remote -v` permite conferir o endereço.
- `git push` envia o commit. Se aparecer uma janela para entrar na conta do GitHub, siga as instruções.

Atualize a página do repositório: os três arquivos devem aparecer.

> Terminou o Caminho B. **Não** faça o Caminho A com essa mesma pasta.

---

## Parte 3 — Trabalhar com branches

Depois de ter o projeto no GitHub (por qualquer um dos caminhos), o ideal é não mexer direto na branch `main`. Em vez disso, criamos uma **branch** para cada tarefa. No Caminho A você já criou uma no passo A4; aqui está o passo a passo completo, para usar sempre que começar uma tarefa nova.

> **Branch** é uma linha de trabalho paralela. Ela permite alterar arquivos e registrar commits sem afetar a `main`, que continua com a versão estável do projeto. Quando o trabalho estiver pronto, ele é levado de volta para a `main`.

### C1. Ver em qual branch você está

```bash
git branch
```

A branch atual aparece com um `*`. Um projeto recém-criado mostra:

```text
* main
```

Para ver também as branches que existem no GitHub, use `git branch -a`.

### C2. Atualizar a main antes de começar

Antes de criar uma branch nova, traga as últimas mudanças do GitHub:

```bash
git switch main
git pull
```

Assim a nova branch parte da versão mais recente do projeto.

### C3. Criar uma branch e mudar para ela

```bash
git switch -c feat/minha-tarefa
```

- `git switch` muda de branch;
- a opção `-c` (*create*) cria a branch antes de mudar;
- `feat/minha-tarefa` é o nome. Escolha um nome curto e descritivo, sem espaços e sem acentos.

Confira com `git branch`: agora o `*` está em `feat/minha-tarefa`.

> **Convenção de nomes:** muitos times usam um prefixo que indica o tipo de trabalho, como `feat/` para uma funcionalidade nova, `fix/` para uma correção e `docs/` para documentação. Por exemplo: `feat/exercicio-listas`, `fix/erro-no-calculo`, `docs/atualiza-readme`.

**Alternativa com o VS Code:** clique no nome da branch no canto inferior esquerdo da janela (geralmente `main`), escolha **Create new branch...**, digite o nome e pressione **Enter**.

**Alternativa com `git checkout`:** o comando equivalente é `git checkout -b feat/minha-tarefa`. Ele funciona em qualquer versão do Git; se `git switch` não for reconhecido no seu computador, use este.

### C4. Trabalhar e registrar as mudanças

Edite os arquivos normalmente e, no terminal, registre as mudanças na nova branch:

```bash
git status
git add .
git commit -m "Adiciona exercicio de listas"
```

Você pode fazer quantos commits quiser. Todos ficam somente na branch `feat/minha-tarefa`.

### C5. Enviar a branch para o GitHub

Na primeira vez, é preciso dizer ao Git qual é a branch correspondente no GitHub:

```bash
git push -u origin feat/minha-tarefa
```

O `-u` cria essa ligação. Nos envios seguintes, basta usar `git push`.

Se você esquecer o `-u`, o Git mostra um aviso dizendo que a branch atual não tem *upstream*; ele já sugere o comando correto. É só copiá-lo e executar.

### O que é um Pull Request?

Um **Pull Request** (PR) é um **pedido para juntar as mudanças de uma branch em outra**, normalmente da sua branch para a `main`. O nome vem de "pedir para *puxar* (pull) as minhas mudanças". Ele existe no GitHub, não no Git: é uma página onde o pedido fica registrado.

Em vez de juntar as mudanças direto, você abre um PR e, na mesma página:

- vê exatamente **o que mudou**, linha por linha, comparado com a `main`;
- outras pessoas **revisam** o trabalho, deixam comentários e pedem ajustes;
- o projeto pode rodar **testes automáticos** antes de aceitar as mudanças;
- tudo fica **registrado**: quem pediu, quem aprovou e quando foi feito o merge.

> **Analogia:** é como entregar um trabalho para revisão antes de ele entrar na versão final. A `main` continua com a versão aprovada, e só recebe o seu trabalho depois que ele for aceito.

Para juntar as mudanças, o GitHub faz um **merge**: incorpora os commits da sua branch na `main`. O caminho completo é:

```text
criar branch → fazer commits → push → abrir Pull Request → revisão e aprovação → merge na main → git pull na main
```

### C6. Abrir o Pull Request

Com a branch já enviada ao GitHub (passo C5):

1. Abra a página do repositório no GitHub. Logo depois do `push`, aparece um aviso amarelo com o botão **Compare & pull request**. Clique nele.
   Se o aviso não aparecer, vá na aba **Pull requests** e clique em **New pull request**.
2. Confira os dois campos no alto da página: a **base** deve ser `main` (para onde as mudanças vão) e o **compare** deve ser a sua branch (de onde elas vêm).
3. Escreva um **título** curto e, na descrição, explique o que foi feito e por quê.
4. Se quiser, escolha quem vai revisar em **Reviewers** (barra lateral direita).
5. Clique em **Create pull request**.

O PR criado fica na aba **Pull requests** do repositório. Ele tem três abas principais:

| Aba | O que mostra |
| --- | --- |
| **Conversation** | A descrição, os comentários e o botão de merge. |
| **Commits** | Os commits incluídos no PR. |
| **Files changed** | As mudanças, arquivo por arquivo. |

### C7. Revisar e aprovar

Quem revisa (uma pessoa do time, o professor ou a professora) confere as mudanças antes de aceitá-las:

1. Na aba **Pull requests**, clique no PR que quer revisar.
2. Abra a aba **Files changed**. Linhas em **verde** foram adicionadas e linhas em **vermelho** foram removidas.
3. Para comentar uma linha específica, passe o mouse sobre ela e clique no botão **+** azul que aparece ao lado do número.
4. Ao terminar, clique em **Review changes** (canto superior direito), escreva um comentário, se quiser, e escolha uma opção:
   - **Comment**: só deixa observações, sem aprovar nem bloquear;
   - **Approve**: aprova as mudanças;
   - **Request changes**: pede ajustes antes de aceitar.
5. Clique em **Submit review**.

> **Atenção:** o GitHub não deixa você aprovar o **seu próprio** PR. A aprovação precisa vir de outra pessoa. Em um repositório só seu, sem regras de aprovação, você pode fazer o merge direto, sem esse passo.

**Se pedirem ajustes**, não abra outro PR: volte à sua branch, edite os arquivos, faça novos `add` e `commit` e envie com `git push`. Os novos commits aparecem automaticamente no mesmo PR, e a pessoa pode revisar de novo.

### C8. Fazer o merge

Com o PR aprovado, volte à aba **Conversation**:

1. Se aparecer a mensagem **This branch has no conflicts with the base branch**, está tudo certo para juntar.
2. Clique em **Merge pull request** e depois em **Confirm merge**.
3. O GitHub mostra **Pull request successfully merged and closed**. Nesse momento, as mudanças já estão na `main` **do GitHub**.
4. Clique em **Delete branch**, que aparece logo abaixo, para apagar a branch do GitHub: ela já cumpriu o papel.

> **Conflitos:** se aparecer **This branch has conflicts that must be resolved**, a `main` foi alterada nas mesmas linhas que você mexeu. Peça ajuda a quem revisa antes de continuar: é preciso escolher qual versão de cada trecho vai ficar.

### C9. Voltar para a main e pegar as mudanças

O merge aconteceu **no GitHub**. A `main` do seu computador continua como estava antes, sem os itens novos, até você atualizá-la:

```bash
git switch main
git pull
```

- `git switch main` volta para a branch principal (ou `git checkout main`);
- `git pull` traz do GitHub tudo o que foi juntado na `main`: o seu trabalho e o de outras pessoas.

Para conferir, veja o último commit:

```bash
git log --oneline -3
```

Deve aparecer uma linha parecida com `Merge pull request #3 from ...feat/minha-tarefa`. Os arquivos também aparecem no Explorador do VS Code.

Depois, apague a branch local, que não é mais necessária:

```bash
git branch -d feat/minha-tarefa
git fetch --prune
```

- `git branch -d` apaga a branch **no seu computador**;
- `git fetch --prune` remove as referências às branches que já foram apagadas no GitHub.

Pronto: a `main` do computador está igual à do GitHub. Para a próxima tarefa, volte ao passo C2 e crie uma nova branch.

### Problemas comuns

| Mensagem ou situação | O que fazer |
| --- | --- |
| `fatal: a branch named '...' already exists` | Esse nome já existe. Use outro nome, ou mude para a branch existente com `git switch nome`. |
| `Your local changes ... would be overwritten` ao trocar de branch | Há alterações não salvas no Git. Faça `git add .` e `git commit` antes de trocar de branch. |
| `The current branch ... has no upstream branch` | Faltou o `-u` no primeiro push. Execute `git push -u origin nome-da-branch`. |
| Fiz alterações e percebi que estava na `main` | Antes de fazer o commit, crie a branch com `git switch -c nome`: as alterações vão junto para a nova branch. |
| Não sei em qual branch estou | Rode `git branch` ou `git status`. |
| Não aparece o botão **Compare & pull request** | Confira se o `git push` da branch foi feito. Depois, vá em **Pull requests** e clique em **New pull request**. |
| Não consigo aprovar o meu PR | O GitHub não permite aprovar o próprio PR. Peça a outra pessoa. Em repositório só seu, faça o merge direto. |
| Fiz o merge, mas os arquivos não estão no meu computador | Falta atualizar a `main` local: rode `git switch main` e `git pull`. |
| `git pull` diz `Already up to date`, mas o PR foi aceito | Confira se você está na `main` (`git branch`) e se o PR aparece como **Merged** no GitHub, e não como **Open**. |
| `error: the branch '...' is not fully merged` ao apagar a branch | Confira no GitHub se o PR foi mesmo mesclado. Se foi, apague com `git branch -D nome`. |
