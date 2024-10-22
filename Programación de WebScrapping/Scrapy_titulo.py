import scrapy

class CitasSpider(scrapy.Spider):
    
    name = "citas"
    start_urls = ['http://quotes.toscrape.com/']
    custom_settings = {
        "LOG_ENABLED": False,
    }
    
    def parse(self,respuesta):
        titulo_pagina = respuesta.css("title::text").get()
        print(f"Titulo de la pagina: {titulo_pagina}")
