# certificate_maker_cli

Script para geração de certificados a partir de um template HTML e uma imagem de fundo. (Apenas Windows)

___


## Uso
Quatro parâmetros são necessários para a execução do programa:

- Caminho para o CSV com os dados
    - O CSV deve ter os valores separados por vírgula ```','``` e os valores de texto delimitados por aspas duplas ```'"'```
- Caminho para o HTML que servirá de esqueleto para estruturar os dados
    - Para inserir os dados do CSV no HTML, deve-se usar o padrão ```%__HEADERNAME__%```.
    - Ex.: Se no CSV tiver uma coluna com o cabeçalho chamado ```NAME``` com os nomes dos participantes do evento, no HTML deve estar indicado como ```%__NAME__%```
- Caminho para a imagem que ficará de fundo no certificado
- Padrão de nome dos arquivos gerados
    - De forma parecida com inserir dados dentro do HTML, o padrão de nomes deve usar o nome do cabeçalho do CSV, mas sem a estrutura ```%__...__%```.
    - Ex.: ```"DATE - NAME"```

Um exemplo de chamada ao script seria:

```python index.py .\data.csv .\template.html .\background.png "EVENT - NAME"```

___

### Cuidados

O HTML a ser usado pode ser definido pelo próprio usuário, porém um template de exemplo está disponível no [Gist](https://gist.github.com/Ellyzeul/70ec010ca24e44a4f43f90f30071d5e2)

O projeto utiliza a ferramenta wkhtmltopdf, uma ferramenta open-source para a conversão de documentos HTML em documentos PDF, repositório disponível em: https://github.com/wkhtmltopdf/wkhtmltopdf

Essa ferramenta é bastante completa em alguns aspectos, mas não é perfeita. Dois maiores problemas são:

- Ao gerar um PDF na direita haverá uma coluna de 1px e no rodapé haverá uma linha de 1px, ambas em branco

- Não entende corretamente as propriedades CSS ```margin``` e ```padding```, portanto para posicionamento de elementos é necessário definir o elemento como ```position: absolute``` e definir seu posicionamento pelas propriedades ```left``` e ```top```

Ambos os problemas estão sendo estudados pelo autor do projeto, mas sem previsão de quando serão desenvolvidos. (Issue do [primeiro problema](https://github.com/wkhtmltopdf/wkhtmltopdf/issues/5088) e issue do [segundo problema](https://github.com/wkhtmltopdf/wkhtmltopdf/issues/1606))

Por conta desse segundo problema, não é possível utilizar flex nem grid para posicionamento centralizado dos elementos.
