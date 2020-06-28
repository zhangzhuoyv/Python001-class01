# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpidersPipeline:
    def process_item(self, item, spider):
        # 把 item 信息传入管道
        name = item['name']
        tag = item['tag']
        time = item['time']

        #output 定义输出内容 title ,link ,content ，并赋予给output
        output = f'|{name}|\t|{tag}|\t|{time}|\n\n' #这里不是很明白，就知道\t是制表符，可能后面课程会教

        # encoding (编码) 为 utf-8, 并把这个动作赋予格局article
        with open('./top10_film_info2.csv','a+', encoding='utf-8') as article:
            article.write(output)  # 输出 output的内容
        return item  # 这里必须返回item ，否则或报错 dorp item














        return item
