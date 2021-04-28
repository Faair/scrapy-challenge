
# -*- coding: utf-8 -*-
 
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
 
import scrapy
 
class AmazonItem(scrapy.Item):
  # define the fields for your item here like:
  product_name = scrapy.Field()
  product_link = scrapy.Field()
  image_link = scrapy.Field()
  term_ranking = scrapy.Field()
  ranking_percent = scrapy.Field()
  actual_ranking = scrapy.Field()
  previous_ranking = scrapy.Field()
  ranking_average = scrapy.Field()
  rate_qty = scrapy.Field()
  number_of_offers = scrapy.Field()
  lowest_price = scrapy.Field()
  max_price = scrapy.Field()