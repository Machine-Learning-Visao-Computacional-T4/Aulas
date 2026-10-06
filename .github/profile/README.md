# Machine Learning e Visão Computacional — Turma T4

Bem-vindo(a) ao GitHub da **Turma T4** do curso *Machine Learning e Visão Computacional* (SC TEC, execução SENAI).

Aqui ficam os **exercícios de cada semana**, com **guias passo a passo** de como executar cada um e **soluções de exemplo** para você conferir depois de tentar sozinho(a). Este GitHub também serve como **exemplo de organização**: é assim que um projeto bem arrumado aparece para quem o visita.

---

## Os repositórios do curso

Cada semana tem o seu próprio repositório.

| Semana | Tema | Repositório |
| --- | --- | --- |
| 01 | Aula inaugural e fundamentos de IA, ML e DL | *(conceitual, sem exercícios de código)* |
| 02 | O pipeline de ML: do problema ao dataset, métricas, overfitting e produção | [semana-02-pipeline-ml](https://github.com/Machine-Learning-Visao-Computacional-T4/semana-02-pipeline-ml) |
| 03 | Lógica de programação com Python: variáveis, operadores, condicionais e loops | [semana-03-logica-python](https://github.com/Machine-Learning-Visao-Computacional-T4/semana-03-logica-python) |
| 04 | Git, GitHub, Python local, VS Code e estruturas de dados | [semana-04-git-github-estruturas](https://github.com/Machine-Learning-Visao-Computacional-T4/semana-04-git-github-estruturas) |
| 05 | Arquivos (texto, CSV, JSON), datas, regex, funções e módulos | [semana-05-arquivos-datas-funcoes](https://github.com/Machine-Learning-Visao-Computacional-T4/semana-05-arquivos-datas-funcoes) |

Os repositórios das próximas semanas serão adicionados aqui ao longo do curso.

## Materiais complementares

Slides, arquivos de apoio e outros materiais do curso estão na **pasta do Google Drive da turma**:

[Abrir a pasta "ML T4" no Google Drive](https://drive.google.com/drive/folders/1N9Qw0RVML5Ea5bXbAd0ffmPz6zDIpUF3?hl=pt-br)

---

## Como usar este GitHub

### 1. Encontre o repositório da semana
Na tabela acima, clique no repositório. Na página dele você vê:
- o **`README.md`** da semana (o que será estudado e como executar);
- as pastas **`aula1_...`, `aula2_...`, `aula3_...`**, uma por aula;
- dentro de cada aula, uma pasta por **exercício**, com um `README.md` que traz o **objetivo**, o **passo a passo**, **dicas** e um **exemplo de execução**.

### 2. Faça a sua cópia (fork)
Para praticar sem mexer no material original, crie a **sua cópia**:
1. Entre no repositório da semana e clique em **Fork** (canto superior direito).
2. Confirme. O GitHub cria `seu-usuario/nome-do-repositorio` na **sua conta**.

### 3. Traga para o seu computador (clone)
```bash
git clone https://github.com/SEU_USUARIO/semana-03-logica-python.git
cd semana-03-logica-python
```
Ou, no **GitHub Desktop**: *File → Clone Repository*. Ou, no **VS Code**: `Ctrl + Shift + P` → *Git: Clone*.

### 4. Execute um exercício
```bash
python aula3_condicionais_loops/exercicio_06_fizzbuzz/fizzbuzz.py
```
No Windows, se `python` não funcionar, use `py`. Se preferir, use o **Google Colab** (sem instalar nada): cole o código em uma célula e execute com `Shift + Enter`.

> **Tente sozinho(a) primeiro.** Só depois olhe a solução de exemplo. A sua pode ser diferente e estar certa.

### 5. Salve o seu trabalho (commit e push)
O fluxo que você repete em **todo** exercício: **código → teste → commit → push**.

```bash
git add .
git commit -m "Resolve o exercício de FizzBuzz"
git push
```
Atualize a página do **seu** repositório no navegador e confira se a mudança apareceu. Se quiser, o passo a passo completo está na [Semana 04](https://github.com/Machine-Learning-Visao-Computacional-T4/semana-04-git-github-estruturas).

### 6. Receba as novidades do repositório original
Quando um repositório da turma for atualizado, na página do **seu fork** clique em **Sync fork → Update branch**. Depois, no computador:
```bash
git pull
```

---

## Ordem de estudo sugerida
1. Leia o `README.md` da **semana**.
2. Siga as **aulas na ordem**: cada uma prepara a seguinte.
3. Em cada exercício: leia o guia, **tente**, depois **compare** com a solução.
4. Faça **commit e push** do que produzir.

## Combinados de boa convivência
- Use **somente dados fictícios** nos exercícios que vão para o GitHub.
- **Nunca** suba senhas, chaves ou tokens de acesso. Se um dia isso acontecer, apague o token e crie outro.
- Commits **pequenos e com mensagens claras** (`Adiciona exercício de listas`, e não `mudanças`).

## Dúvidas
Leve suas dúvidas para a aula ao vivo ou para os canais da turma. Ao pedir ajuda, **copie a mensagem de erro** completa e diga o que você já tentou.
