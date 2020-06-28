# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from spiders.items import SpidersItem



class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    # def parse(self, response):
    #     pass

    #开始第一个请求函数
    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        cookie = {
            "__mta": "119806007.1593107842173.1593161979973.1593161980009.10",
            "uuid_n_v": "v1",
            "uuid": "4CE7F7F0B70D11EA9B3075693A212BAFD840DB84EF7745AE8C6E0232A8675E7C",
            "_csr": "f61d9a8c249a5f79121e023b66d09dbe7b9686863d566aadb34ea3d63665ba07",
            "mojo-uuid": "cba42ebfbac7499726e6f55dac5fb937",
            "_lxsdk_cuid": "172eca072f0c8-0134bf7889df4-31617402-13c680-172eca072f1c8",
            "_lxsdk": "4CE7F7F0B70D11EA9B3075693A212BAFD840DB84EF7745AE8C6E0232A8675E7C",
            "Hm_lvt_703e94591e87be68cc8da0da7cbd0be2": "1593171654,1593174010,1593189473,1593228626",
            "mojo-trace-id": "4",
            "Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2": "1593228965",
            "__mta": "119806007.1593107842173.1593161980009.1593228965406.11",
            "_lxsdk_s": "172f3d3885e-182-eff-2e8%7C%7C5"
        }

        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False,cookies=cookie)
        #yield 的作用，是把结果返回给下面的 方法，我理解为一个迭代器

        # scrapy.Request 是内部功能，跟request库 类似，都是向网页发出访问请求
        # callback = self.parse , 把结果 传递给 内部（self) 方法函数 parse 处理
        # dont_filter = False 意思是 是否不去重（URL） ，设置是否。 意思就是地址去重
        # 这里加多一个cookies  ,因为被反爬折腾怕了，加了保险点，不知道是否起作用 - -｜｜

    # 解释方法 parse ,接受网页返回的 response,

    def parse(self, response):
        print(response.text) # 单步调试的时候，用来看，是否抓取到内容，避免之前多次运行后，被反爬，怕了- -｜｜
        items = [] #用来 装载 的 item ：电影名，类型，上映时间
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        # Selector 配 xpath ，相当于 beautiful soup 配 find_all , 但是更简介，功能更强大
        # response =response ,这里直接 传入 respone,而不需要 reponse.text,因为 xpath 从一开始就是按照 xml 格式处理
        # xpath('//div[@class="movie-hover-info"]')就是从第一个<div>开始匹配 。 [@class="movie-hover-info"]') ,就是 需要满足 属性 class 的 值 是 movie-hover-info,才去匹配
        # 把匹配到的 所有符合条件的 <div> 赋予 给 movies

        cont = 0 # 计数器，用来抓取10个电影就停止

        for movie in movies: # 把刚才爬去到的<div>, 一个一个地给 movie
            item = SpidersItem() #引用 items.py 里面类函数 SpidersItem()，赋予给 item

            item['name'] = movie.xpath('./div[1]/span[1]/text()').extract()[0]
            #抓取 相对路径（//div[@class="movie-hover-info）下的，第一个<div>,第一个<span>的文本标签，并赋予给 item[name],也就是 "name = scrapy.Field()"
            #.extract() 返回一个lsit ,而不是SelectorList（为了可读性）extract()[0]，就是列表中第一个元素


            item['tag'] = movie.xpath('./div[2]/text()').extract()[1].strip('\n').strip(' ').strip('\n')
            # 抓取相对路径的 第二个<div>的文本信息，用extract()转化成 list,并去第二个元素，去掉换行符，空格，换行符
            # 赋予给 item['tag'], 也就是 "type = scrapy.Field()"

            item['time'] = movie.xpath('./div[4]/text()').extract()[1].strip('\n').strip(' ').strip('\n')
            #抓取相对路径的 第四个<div> 的文本信息，用extract()转化成 list,并去第二个元素，去掉换行符，空格，换行符
            # 赋予给 item['time'], 也就是 "time = scrapy.Field()"

            items.append(item)
            # 把上面抓取的 name tag time ，追加列表 items

            cont += 1 #完成一轮抓取，计数器+1

            # 抓到第10次就停止
            if cont ==9:
                break

            return items # 指定动作，返回到列表 items











        
        
