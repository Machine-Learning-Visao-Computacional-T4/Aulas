# Exercício 03 — Mapeie o ciclo de vida de um modelo

**Tipo:** estudo de caso

## Cenário
Uma plataforma de **streaming de filmes e séries** usa um modelo de ML para **recomendar conteúdo**. As recomendações aparecem na tela inicial ("Recomendados para você", "Porque você assistiu...") e ao final de cada episódio ou filme. A plataforma tem milhões de usuários, em vários países, acessando pelo celular, pela TV e pelo computador. O catálogo recebe dezenas de títulos novos por semana.

## Perguntas
1. **Deploy:** que forma de deploy faz mais sentido: **tempo real**, **lote (batch)** ou **embarcado**? Justifique. Pode ser mais de uma?
2. **Drift:** que sinais de **data drift** (mudança nos dados de entrada) ou **concept drift** (mudança na relação entre os dados e o que o usuário realmente quer) poderiam aparecer com o tempo? Dê pelo menos **um exemplo de cada**.
3. **Retreino:** quando faria sentido retreinar o modelo? Por **calendário fixo**, por **queda de desempenho**, ou por **algum evento específico**?

## Passo a passo
1. Crie `minhas_respostas.md` nesta pasta com as três respostas.
2. Em cada resposta, escreva **o raciocínio**, não só a escolha ("batch porque...").
3. Compare com um colega e discuta onde vocês discordaram.

## Dica
Os mesmos conceitos valem para qualquer domínio: o que muda é o **custo de errar** e a **velocidade com que o mundo muda**.
