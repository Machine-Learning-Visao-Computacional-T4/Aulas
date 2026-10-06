# Exercício 08 — Quiz relâmpago: revisão do Módulo 05

Cobre as 3 aulas (arquivos, datas e regex, funções e módulos).

1. Qual a diferença entre `print` e `return`?
2. Qual a diferença entre o modo `"w"` e o modo `"a"` ao abrir um arquivo?
3. O que `strptime` faz? E `strftime`?
4. O que `\D` faz em uma regex?
5. Por que usar `with open(...)`?
6. Para que serve `newline=""` ao abrir um CSV?
7. Qual a diferença entre `json.dump` e `json.dumps`?
8. O que o bloco `if __name__ == "__main__":` faz?
9. **Preveja a saída:**
   ```python
   def f(x, y=2):
       return x * y

   print(f(3), f(3, 4), f(y=5, x=1))
   ```
10. Qual o erro mais comum quando um `import` de módulo próprio falha?

<details>
<summary>Ver respostas</summary>

1. `print` **mostra** na tela e devolve `None`; `return` **devolve** o valor para quem chamou a função.
2. `"w"` **apaga** o conteúdo anterior e escreve; `"a"` **acrescenta** ao final.
3. `strptime` converte **texto em data**; `strftime` converte **data em texto**.
4. Casa **qualquer caractere que não seja dígito**.
5. Fecha o arquivo automaticamente ao fim do bloco, mesmo se houver erro.
6. Evita **linhas em branco extras** no Windows.
7. `dump` grava em um **arquivo**; `dumps` devolve um **texto** JSON.
8. Roda o código dentro dele **só** quando o arquivo é executado direto, e não quando é importado.
9. `6 12 5`.
10. O módulo e quem o importa **não estão na mesma pasta** (ou o nome do arquivo está errado).

</details>

> As perguntas foram preparadas para este repositório. Crie as suas e troque com colegas.
