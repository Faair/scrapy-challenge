import scrapy
from ps_atoz.items import AmazonItem
import re



def get_rate_qty(response):
    rate_qty = []
    number_of_comments1 = response.css('.a-link-normal::text').extract()
    for j in range(len(number_of_comments1)):
        number_of_comments = response.css('.a-link-normal::text')[j].extract()
        rate_str = str(number_of_comments)
        if '\n' not in rate_str and 'em' not in rate_str:
            rate_qty.append(rate_str)
    return rate_qty



def get_product_link(response):
    product_link = []
    for j in range(50):
        product_link1 = response.css('.a-link-normal::attr(href)')[j].extract()
        product_str = str(product_link1)
        string = 'https://www.amazon.com.br' +str(product_str)
        product_link.append(string)
    return product_link



def get_price(response):
    price_list = []
    lowest_price = []
    max_price = []
    for j in range(50):
        price = response.css('.zg-item-immersion:nth-child(%d) .a-color-price'% j).css('::text').extract()
        price_str = str(price)
        if '-' in price_str:
            x = price_str.replace(",",".") # replacing ',' by '.'
            y = re.findall(r"[-+]?\d*\.\d+|\d+", x)  # finding floating numbers
            lowest_price.append(y[0])
            max_price.append(y[1])
        else:
            lowest_price.append(None)
            max_price.append(None) 
    return max_price, lowest_price



class AmazondataSpider(scrapy.Spider):
    name = 'AmazonData'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com.br/gp/movers-and-shakers/grocery']

    def parse(self, response):
        items = AmazonItem()
        product_name = response.css('img::attr(alt)').extract()      
        image_link = response.css('img::attr(src)').extract()
        term_ranking = response.css('.zg-badge-text::text').re("#(\d+)")
        ranking_percent = response.css('.zg-percent-change::text').re("(.*?)\%")
        actual_ranking = response.css('.zg-sales-movement::text').re("vendas: (\d+)") 
        previous_ranking = response.css('.zg-sales-movement::text').re("anterior: (\d+)") 
        ranking_average = response.css('.a-icon-alt::text').re("(.*?)\ de")
        #number_of_offers = response.css('') # is not applied (missing HTML)

        product_link = get_product_link(response)
        rate_qty = get_rate_qty(response)
        max_price = get_price(response)
        lowest_price = get_price(response)       
       
        items['product_name'] = product_name
        items['product_link'] = product_link
        items['image_link'] = image_link
        items['term_ranking'] = term_ranking
        items['ranking_percent'] = ranking_percent
        items['actual_ranking'] = actual_ranking
        items['previous_ranking'] = previous_ranking
        items['ranking_average'] = ranking_average
        items['rate_qty'] = rate_qty
        items['max_price'] = max_price
        items['lowest_price'] = lowest_price

        yield items