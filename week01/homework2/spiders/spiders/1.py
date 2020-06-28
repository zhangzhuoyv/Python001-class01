# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import requests
import random
import pandas as pd

angents = [
    "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
]
user_agent = random.choice(angents)

cookie = '__mta=251492665.1593162041862.1593221217757.1593222711821.12; uuid_n_v=v1; uuid=821BAB50B78B11EAB11C23537EB4C64B6C0C6CF47A73446D9E1F236B2228DC37; _csrf=385e4522361eb8fde444a8e5300cfaaf61d627c0aad8c22295238edcf4ed970d; mojo-uuid=d1bd32496ef4c7cea4bcfbf1d24397d7; _lxsdk_cuid=172efdb89f1c8-0e53d2a767a3bd-31617402-13c680-172efdb89f1c8; _lxsdk=821BAB50B78B11EAB11C23537EB4C64B6C0C6CF47A73446D9E1F236B2228DC37; lt=B10T4yXQNEeK7Z05NhZqJTU8o-oAAAAA5woAAJr-o1rwpvC3gBxgkmg826wNg_W6vX9jXMTU9yYLrxKb-hdyWrNhMbMlSW-yJDSewA; lt.sig=qYl0rTxvpURUV02R7WZWKtq8Kdc; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593171644,1593171741,1593171960,1593172899; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; mojo-session-id={"id":"21f245091f37f4c8ec104aaa4e993d16","time":1593259855805}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593259861; __mta=251492665.1593162041862.1593222711821.1593259861396.13; _lxsdk_s=172f5b01165-0e1-78c-fc8%7C%7C6'

# http头部 伪装浏览器

header = {'Ueser-agent': user_agent, 'cookie': cookie}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(url=myurl, headers=header)

response.encoding = 'utf-8'


bs_info = bs(response.text, 'html.parser')

#用来装 抓取到的电影的名称，类型，时间
top10_movie_info = []

#后面用来把信息排序
name = ['name', 'type', 'time']

cont = 0 #用来抓取 10个电影信息后停止

for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):

    # div_child_tags 是 tags.find_all('div') 处理后的，一个列表
    div_child_tags = tags.find_all('div')


    #按照div和其标签内的text索引，去取值。（每个 attrs={'class': 'movie-hover-info'} 的<div>结构相同

    # 在div_child_tags 里，第一个<div>里（以换行符分隔），提取第二个文本信息（精简掉前后空格），赋予给 file_name
    file_name = div_child_tags[0].text.split('\n')[1].strip(' ')

    # 在div_child_tags 里，第二个<div>里（以换行符分隔），提取第三个文本信息（精简掉前后空格），赋予给 file_type
    file_type = div_child_tags[1].text.split('\n')[2].strip(' ')

    # 在div_child_tags 里，第四个<div>里（以换行符分隔），提取第三个文本信息（精简掉前后空格），赋予给 file_type
    file_time = div_child_tags[3].text.split('\n')[2].strip(' ')

    # 把 file_name, file_type, file_time 追加在 列表 top10_movie_info
    top10_movie_info.append([file_name, file_type, file_time])

    #进入下一次循环
    cont+=1

    # 如果循环够10次了，就退出循环
    if cont>10:
        break

# 用 pandas 的 DataFrame 列表 top10_movie_info ，处理为二维数据

movie_data = pd.DataFrame(columns=name,data = top10_movie_info)

#把 movie_data 保存到本地

movie_data.to_csv('top10_movie_info',encoding='utf-8')


















