# -*- coding: utf-8 -*-
import scrapy
from movies.items import MoviesItem
from scrapy.spidermiddlewares.httperror import HttpError

class MaoyanSpider(scrapy.Spider):

    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
    movie_url = 'https://maoyan.com/films?showType=3'
    def start_requests(self):
        header = {
            'Accept':"*/*",
            'Accept-Encoding':'gazip,deflate,br',
            'Accept-Language':'en-AU,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6',
            'Content-Type':'text/plain',
            'Connection':'keep-alive',
            'Origin':'https://maoyan.com',
            'Referer':'https://maoyan.com/films?showType=3',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'cross-site'
        }
         # 添加请求异常的处理错误回调函数
        yield scrapy.Request(url=self.movie_url, headers=header, callback=self.parse, errback=self.errback, dont_filter=False)

    def parse(self, response):
        # print(response.text)
        dl = response.selector.xpath('//div[@class=\'movie-hover-info\']')
        
        if dl:
            for dd in dl:
                item = MoviesItem()
                item['movie_name'] = dd.xpath('div[1]/@title').extract_first().strip()
                item['movie_type'] = dd.xpath('div[2]/text()[2]').extract_first().strip()
                item['movie_time'] = dd.xpath('div[4]/text()[2]').extract_first().strip()
                yield item
        
            
            

    def errback(self, failure):     
        request_url = failure.request.url
        record = {
                'url': request_url,
                'response': 0
        }
        if failure.check(HttpError):
             # 记录响应码非200的信息
            response = failure.value.response
            record['response'] = response
            self.logger.error('HttpError is %s', repr(record))
        else:
             # 记录所有错误回调信息，将错误信息转为字符串存储日志
            self.logger.error('OtherError is %s',repr(failure))
        