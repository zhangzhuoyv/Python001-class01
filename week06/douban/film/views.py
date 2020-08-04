from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from django.http import HttpResponse

from .models import Movie, T1

from django.db.models import Avg


# Create your views here.
def index(request):
    # return HttpResponse ('hello,this is index!')
    return render(request, 'index.html')


# path(<int:year>,views.year)

def year(request, year):
    # return HttpResponse(year)
    return redirect('2020.html')  # 可重定向页面


# path('<int:year>/<str:name>', views.name),
# 接收不定长参数
def name(request, **kwargs):
    return HttpResponse(kwargs['name'])


# path('<myint:year>', views.year),
# re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),

def myyear(request, year):
    return render(request, 'yearview.html')


def movies(request):
    ### 从models取数据传给 template ###
    n = Movie.objects.all
    return render(request, 'movieslist.html', locals())  # locals() 本地所有变量，这里只有n


def books_short(request):
    ###  从models取数据传给template  ###
    shorts = T1.objects.all()
    # 评论数量
    counter = T1.objects.all().count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg = f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    # 情感倾向
    sent_avg = f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # 正向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())


def week06(request):
    ###  从models取数据传给template  ###
    shorts = T1.objects.all()

    # 评论数量
    counter = T1.objects.all().count()

    queryset = T1.objects.values('n_star')
    conditions = {'n_star': 4}
    four_star = queryset.filter(**conditions).count()

    queryset = T1.objects.values('n_star')
    conditions = {'n_star': 5}
    five_star = queryset.filter(**conditions).count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg = f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "

    # 情感倾向
    sent_avg = f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    high_start = four_star + five_star

    return render(request, 'week06.html', locals())


def search(request):







    q = request.GET.get('q')

    shorts = T1.objects.filter(short__contains=q)

    # 评论数量
    counter = T1.objects.filter(short__contains=q).count()

    queryset = T1.objects.filter(short__contains=q).values('n_star')
    conditions = {'n_star': 4}
    four_star = queryset.filter(**conditions).count()

    queryset = T1.objects.filter(short__contains=q).values('n_star')
    conditions = {'n_star': 5}
    five_star = queryset.filter(**conditions).count()

    high_start = four_star + five_star


    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg = f" {T1.objects.filter(short__contains=q).aggregate(Avg('n_star'))['n_star__avg']:0.1f} "

    # 情感倾向
    sent_avg = f" {T1.objects.filter(short__contains=q).aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "
    #
    # return render(request, 'search_result.html',
    #               {'shorts': shorts, 'star_avg': star_avg, 'sent_avg': sent_avg, 'sent_avg': sent_avg,
    #                'high_start': high_start,'counter':counter,'four_star':four_star,'five_star':five_star})

    return render(request,'search_result.html',locals())

# {'star_avg': star_avg}, {'sent_avg': sent_avg}, {'sent_avg': sent_avg}, {'high_start': high_start})
