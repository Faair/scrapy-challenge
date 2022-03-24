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
## Introdução
Neste repositório foi desenvolvido um crawler para extração de dados da página da Amazon utilizando a biblioteca Scrapy do Python. Foram extraídos os seguintes dados:

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
