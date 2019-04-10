# -*- coding: utf-8 -*-
import scrapy


class TorrescabralSpider(scrapy.Spider):
    name = 'TorresCabral'
    allowed_domains = ['www.torrescabral.com.br']
    start_urls = ['http://www.torrescabral.com.br/']








    def parse(self, response):
        for link in response.css(' ul.nivel-um li ::attr(href)').getall():
            yield response.follow (link,self.parse_product_links)


    def parse_product_links(self,response):
        for link in response.css('div.acoes-produto ::attr(href)').getall():
            yield response.follow(link,self.parse_items)


    def parse_items(self,response):
        titulo = response.css('section div h1::text').getall()
        reais = response.css('span.preco-avista span::text').get()
        centavos = response.css('span.preco-avista span span span span::text').get()
        yield {"titulo":titulo,'valor':(reais+','+centavos)}
















