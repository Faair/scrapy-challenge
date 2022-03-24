# Desafio Python Web Scrapy
***

## Instalação (Linux)
1. Clonar este repositório e entrar na pasta
2. Criar ambiente virtual
```
python3 -m venv .venv
```
3. Ativar ambiente virtual
```
source .venv/bin/activate 
```
4. Instalar dependências
```
python3 -m pip install requirements.txt
```

## Descrição
A Amazon tem uma [página](https://www.amazon.com.br/gp/movers-and-shakers) que é atualizada de hora em hora onde são mostrados os produtos que mais subiram de ranking. Esses resultados são separados em categorias, como por exemplo [Alimentos e Bebidas](https://www.amazon.com.br/gp/movers-and-shakers/grocery). Alguns exemplos de como um item pode aparecer no ranking: 

![Exemplo de item 1](https://i.imgur.com/E4EmoNY.png)![Exemplo de item 2](https://i.imgur.com/ws5tn55.png)
![Exemplo de item 3](https://i.imgur.com/oMxLF92.png)

Neste repositório foi desenvolvido um crawler para extração de dados da página da Amazon utilizando a biblioteca Scrapy do Python. São extraídos os seguintes dados:

 - Nome
 - Link do produto 
 - Link da imagem 
 - Rank no termometro 
 - Porcentagem de mudança do rank 
 - Rank atual na categoria
 - Rank anterior na categoria 
 - Média de avaliação 
 - Quantidade de avaliações 
 - Quantidade de ofertas 
 - Preço mínimo 
 - Preço máximo 

Após isso, gerou-se um arquivo .json com os seguintes formatos para cada item:

```json
{
    'name': string,
    'link': string,
    'image_link': string,
    'thermometer_rank': integer,
    'recent_category_rank': integer,
    'past_category_rank': integer,
    'rank_percent_change': integer,
    'average_rate': Optional[float],
    'rate_qty': Optional[integer],
    'offers_qty': Optional[integer],
    'min_price': Optional[float],
    'max_price': Optional[float]
}
```

 - Qualquer dúvida, basta entrar em contato através do e-mail: amavickto.fair@gmail.com 
