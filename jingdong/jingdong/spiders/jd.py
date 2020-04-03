# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['www.jd.com']
    start_urls = ['https://www.jd.com/']

    def parse(self, response):
        url = 'https://www.jd.com/'
        yield SplashRequest(url=url,
                            callback=self.parseSecond,
                            args={
                                'wait': 0.5,
                                'url':url,
                                'http_method': 'GET',
                            },
                            endpoint='render.html'
                            )

    def parseSecond(self,response):
        content = response.text
        print(content)