# -*- coding: utf-8 -*-
import scrapy
import re


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    html = 'fiction'
    allowed_domains = ['https://www.goodreads.com/genres/']
    start_urls = ['https://www.goodreads.com/genres/' + html + '//']

    def parse(self, response):
        titles = response.css('img::attr(alt)').extract()
        print(titles, '\n')
        srcs = response.css('img::attr(src)').extract()
        ids = []
        for src in srcs[:5]:
        	match = re.search(r'/books/([\d]+l)', src);
        	ids.append(match.group(1))
        print(ids, '\n')
