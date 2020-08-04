from django.urls import path,re_path,register_converter,translate_url
from .import views,converters

# 创建 自定义过滤类型
register_converter(converters.IntConverter,'myint')
register_converter(converters.FourDigitYearConverter,'yyyy')



urlpatterns = [
    path('',views.index),

    ###带变量的 url
    # path('<int:year>',views.year),  # 只接收整数，其他类型返回404

    path('<int:year>/<str:name>',views.name), #无论输入 int 还是 str, 都跳转到 views.name

    # 正则匹配
    re_path('(?P<year>[0-9]{4}).html',views.myyear,name='urlyear'),

    # 自定义过滤器
    path('<yyyy:year>',views.year),

    path('movies',views.movies),

    path('index',views.books_short),

    path('week06',views.week06),

    path('search',views.search),

]